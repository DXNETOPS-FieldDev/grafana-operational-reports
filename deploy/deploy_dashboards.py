#!/usr/bin/env python3
"""Deploy all Grafana Operational Reports dashboards to a Grafana instance.

Recreates the "Operational Reports" folder tree (idempotent — reuses folders
that already exist by title), pushes every dashboard listed in folder-map.json
into its assigned folder, and health-checks the Spectrum datasource.

Env vars:
  GRAFANA_URL                    e.g. https://grafana.example.com/grafana
  GRAFANA_SERVICE_ACCOUNT_TOKEN  service-account token with Editor/Admin rights
  SSL_CERT_FILE                  (optional) CA bundle path, needed behind a
                                  corporate TLS-inspecting proxy

Usage:
  python3 deploy_dashboards.py [--folder-map folder-map.json] [--dashboards-dir ../dashboards]
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

DATASOURCE_NAME_PATTERN = re.compile(r"^Spectrum (Reporting|MySQL)$")


def api(url, path, token, method="GET", body=None):
    req = urllib.request.Request(url.rstrip("/") + path, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    data = None
    if body is not None:
        req.add_header("Content-Type", "application/json")
        data = json.dumps(body).encode()
    with urllib.request.urlopen(req, data=data) as resp:
        return json.loads(resp.read().decode())


def find_or_create_folder(url, token, title, parent_uid=None):
    path = "/api/folders" + (f"?parentUid={parent_uid}" if parent_uid else "")
    for f in api(url, path, token):
        if f.get("title") == title:
            return f["uid"], False
    body = {"title": title}
    if parent_uid:
        body["parentUid"] = parent_uid
    created = api(url, "/api/folders", token, "POST", body)
    return created["uid"], True


def push_dashboard(url, token, path, folder_uid):
    with open(path) as f:
        content = json.load(f)
    dashboard = content.get("dashboard", content)
    payload = {
        "dashboard": dashboard,
        "overwrite": True,
        "folderUid": folder_uid,
        "message": "Automated deployment via deploy_dashboards.py",
    }
    try:
        return api(url, "/api/dashboards/db", token, "POST", payload), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}: {e.read().decode()[:300]}"


def check_spectrum_datasource(url, token):
    datasources = api(url, "/api/datasources", token)
    matches = [d for d in datasources if DATASOURCE_NAME_PATTERN.match(d["name"])]
    if not matches:
        print("\nWARNING: no datasource named 'Spectrum Reporting' or 'Spectrum MySQL' found.")
        print("Dashboards will show 'Data source not found' until one is created — see")
        print("docs/Deploying-to-a-New-Grafana-Environment.md.")
        return
    for d in matches:
        h = api(url, f"/api/datasources/uid/{d['uid']}/health", token)
        print(f"\nDatasource '{d['name']}' (uid={d['uid']}): {h.get('status')} — {h.get('message')}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--folder-map", default=os.path.join(os.path.dirname(__file__), "folder-map.json"))
    ap.add_argument("--dashboards-dir", default=os.path.join(os.path.dirname(__file__), "..", "dashboards"))
    args = ap.parse_args()

    url = os.environ.get("GRAFANA_URL", "http://localhost:3000")
    token = os.environ.get("GRAFANA_SERVICE_ACCOUNT_TOKEN")
    if not token:
        sys.exit("ERROR: set GRAFANA_SERVICE_ACCOUNT_TOKEN in the environment.")

    with open(args.folder_map) as f:
        fmap = json.load(f)

    root_uid, created = find_or_create_folder(url, token, fmap["root"])
    print(f"Root folder '{fmap['root']}' -> {root_uid} ({'created' if created else 'existing'})")

    jobs = [(d, root_uid) for d in fmap.get("root_dashboards", [])]
    for folder in fmap.get("folders", []):
        sub_uid, created = find_or_create_folder(url, token, folder["title"], root_uid)
        print(f"  Subfolder '{folder['title']}' -> {sub_uid} ({'created' if created else 'existing'})")
        jobs.extend((d, sub_uid) for d in folder["dashboards"])

    print(f"\nDeploying {len(jobs)} dashboards...")
    failures = []
    for fname, folder_uid in jobs:
        path = os.path.join(args.dashboards_dir, fname)
        result, err = push_dashboard(url, token, path, folder_uid)
        if err:
            print(f"  FAIL {fname}: {err}")
            failures.append(fname)
        else:
            print(f"  OK   {fname} -> uid={result['uid']} version={result['version']}")

    print(f"\n{len(jobs) - len(failures)}/{len(jobs)} dashboards deployed successfully.")

    check_spectrum_datasource(url, token)

    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
