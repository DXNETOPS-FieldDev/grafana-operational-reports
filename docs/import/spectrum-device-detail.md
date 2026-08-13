# Device Detail

*Dashboard file: `spectrum-device-detail.json` · Folder: root (not inside a domain folder) · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

## What this shows

A per-device deep-dive: asset info, Availability/Outages/Alarms stat tiles, an outage list, an alarm list, and availability/outage-type pie charts — everything about one device in one place.

## Why this page exists on its own

Ten other dashboards link into Device Detail (Alarm Detail, Alarm Log, Top-N Devices & Models with Most Alarms, Current Assets (Detailed/Customizable), Availability, Availability (Business Hours), Current Chassis-based Assets, Current Ports, Current Ports — Capacity & Idle, Event Log & Top-N Events, Outage Log). Rather than repeat the same "how to import this" text ten times, every other page in this set links back here instead of restating it.

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics (folders, service-account token, deploy script vs. manual import). This page only covers what's specific to Device Detail.
2. Import `spectrum-device-detail.json`. If you're also importing any of the ten dashboards listed above, import this one too — their drill-down links point at it by dashboard **uid** (`spectrum-device-detail`), so it has to exist in your Grafana for the links to resolve.

## Datasource

Reads from a MySQL datasource named **exactly** `Spectrum Reporting` or `Spectrum MySQL` — see [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how the name-based resolution works and how to create the datasource if you don't have one yet.

## Variables

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | Only if your datasource isn't named `Spectrum Reporting`/`Spectrum MySQL` | *(auto-resolves by name)* | Which MySQL connection the panels query. |
| `device` | Not if you always arrive via a drill-down link — those set it for you | *(none)* | The one device this page is about. |

**Opening this page directly** (not via a link): `device` is a single-select dropdown with no "All" option, so on first load it re-queries your own inventory and selects a device from the list rather than showing "no data" — just confirm it's the device you meant, or pick a different one from the dropdown.

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | Datasource variable's saved value is a uid from another Grafana | Load the page once in a browser — Grafana re-resolves `$datasource` by name automatically (see deploy guide) |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or points at the wrong database | Confirm **Save & Test** passes on your datasource and it points at the `reporting` database |
| Page loads but shows the wrong device | Quiet | Reached this page directly rather than via a drill-down link | Pick the right device from the `device` dropdown |
| Numbers differ from what you expected for a given day | Quiet | The database stores timestamps in UTC; the dashboard defaults to your browser's local timezone | Check the dashboard's time range against UTC, not local time, before assuming a data problem |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON. **Don't change the dashboard's uid** if you also import any of the ten linked dashboards — their drill-down links are hardcoded to `spectrum-device-detail` and will break if you rename it.
