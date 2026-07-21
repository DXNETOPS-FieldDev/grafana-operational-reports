# Deploying the Operational Reports to a New Grafana Environment

This guide walks through deploying the full set of Operational Reports
dashboards (Alarm, Availability, Asset, Event, and Service/SLA) to any Grafana
instance — Dev, Production, or a customer's own environment.

## Prerequisites

1. **A running Grafana instance** (tested on Grafana 12.x; OSS or Enterprise
   both work).
2. **A MySQL datasource pointing at the Spectrum `reporting` database**,
   named **exactly** `Spectrum Reporting` or `Spectrum MySQL`. The dashboards
   resolve their datasource by **name** (via a regex match), not by uid, so
   any Grafana instance with a correctly-named datasource works without
   editing the dashboard JSON.
3. **A Grafana service-account token** with **Editor** (or **Admin**) role —
   needed to create folders and push dashboards.
4. Network reachability from the Grafana server to the Spectrum MySQL host
   (test with **Save & Test** on the datasource, or the health-check step
   below).

## Step 1 — Verify the datasource

In Grafana: **Connections → Data sources**, confirm a MySQL datasource named
`Spectrum Reporting` (or `Spectrum MySQL`) exists and click **Save & Test** —
it should report **"Database Connection OK."**

If it doesn't exist yet, create one:
- Type: **MySQL**
- Host: `<spectrum-mysql-host>:3306`
- Database: `reporting`
- User / Password: the read-only reporting credentials for your environment

## Step 2 — Get a service-account token

**Administration → Service accounts** → create one (or reuse an existing
one) → **Add service account token**. Copy the token — Grafana only shows it
once.

## Step 3 — Run the deploy script (recommended)

From the repo root:

```bash
export GRAFANA_URL="https://your-grafana-host/grafana"     # no trailing slash
export GRAFANA_SERVICE_ACCOUNT_TOKEN="<your token>"
# Only needed if your Grafana sits behind a corporate TLS-inspecting proxy
# and you get CERTIFICATE_VERIFY_FAILED errors:
# export SSL_CERT_FILE=/path/to/corporate-ca-bundle.pem

python3 deploy/deploy_dashboards.py
```

This script:
1. Creates the **Operational Reports** folder tree (idempotent — reuses
   folders that already exist by title, so it's safe to re-run).
2. Pushes all 25 dashboards from `dashboards/` into their assigned folders
   (`deploy/folder-map.json` — edit this if you want a different layout).
3. Health-checks the `Spectrum Reporting`/`Spectrum MySQL` datasource and
   reports connectivity.

Expected output ends with something like:

```
25/25 dashboards deployed successfully.

Datasource 'Spectrum Reporting' (uid=...): OK — Database Connection OK
```

### Folder tree it creates

```
Operational Reports
├── Home (Operational Reports — Home) [root]
├── Device Detail (drill-down)         [root]
├── Alarm Reports        (7 dashboards)
├── Asset Reports        (7 dashboards)
├── Availability Reports (5 dashboards)
├── Event Reports        (1 dashboard)
└── Service/SLA Reports  (3 dashboards)
```

## Step 3 (alternative) — Manual import via the UI

If you can't run Python against the target instance, import manually:
1. **Dashboards → New → Import**, upload each file from `dashboards/`.
2. When prompted, select your `Spectrum Reporting` / `Spectrum MySQL`
   datasource.
3. File into folders matching the tree above (optional, but keeps navigation
   links on the Home dashboard consistent).

## Step 4 — Validate

**Always confirm in a live browser — a successful push only proves the JSON
was accepted, not that panels render.**

1. Open the **Home** dashboard (`spectrum-home`) and confirm the report list
   loads.
2. Open **Alarm Log** (or any report) and confirm the stat tiles and table
   show real numbers, not "No data" or "Data source not found."
3. Spot-check one dashboard per domain (Alarm, Availability, Asset, Event,
   Service/SLA) — different panel types (stat, table, bar chart, time
   series) can fail independently.

## Troubleshooting

**Panels show "Data source not found" right after import.**
This is expected on the *very first render* if the dashboard was authored
against a different Grafana instance — the datasource variable's saved
`current.value` is a uid from that other instance. Grafana re-resolves the
variable by **name** (regex `/^Spectrum (Reporting|MySQL)$/`) as soon as the
dashboard loads in a browser, as long as exactly one datasource matches that
name. If it's still broken after a real browser load (not just the API), the
datasource name doesn't match — check Step 1.

**`CERTIFICATE_VERIFY_FAILED` when running the deploy script.**
Your Grafana is behind a corporate TLS-inspecting proxy and Python doesn't
trust its root CA. Export a CA bundle and set `SSL_CERT_FILE` (see Step 3).
On macOS:
```bash
security find-certificate -a -p /System/Library/Keychains/SystemRootCertificates.keychain > /tmp/ca-bundle.pem
security find-certificate -a -p /Library/Keychains/System.keychain >> /tmp/ca-bundle.pem
security find-certificate -a -p ~/Library/Keychains/login.keychain-db >> /tmp/ca-bundle.pem
export SSL_CERT_FILE=/tmp/ca-bundle.pem
```

**Counts don't match the equivalent CABI Report.**
See `docs/Grafana-vs-Jasper-Parity-2026-06-25.md` — almost always a
timezone/time-window difference (dashboards default to the browser's local
timezone; CABI Reports and the database are UTC), not a query bug.

## Repository layout reference

| Path | Purpose |
|---|---|
| `dashboards/*.json` | The 25 dashboard definitions |
| `deploy/deploy_dashboards.py` | Automated deploy script (this guide) |
| `deploy/folder-map.json` | Folder tree + dashboard-to-folder assignments |
| `docs/` | User-facing documentation and CABI-to-Grafana mapping PDFs |
