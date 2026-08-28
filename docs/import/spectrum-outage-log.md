# Outage Log

*Dashboard file: `spectrum-outage-log.json` · Folder: Availability Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

This page links out to **[Device Detail](spectrum-device-detail.md)** (imported separately — see that page); nothing else in this set links into it.

## What this shows

The raw outage ledger, planned or not: total/unplanned/planned/exempt/devices-with-outage tiles and an outage table with an "ongoing" label for outages still in progress. The source-of-truth event list behind the availability numbers, needed for root-cause analysis.

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics (folders, service-account token, deploy script vs. manual import). This page only covers what's specific to Outage Log.
2. Import `spectrum-outage-log.json`, plus `spectrum-device-detail.json` (see **[Device Detail](spectrum-device-detail.md)**) — its per-row drill-down needs it.

## Datasource

Reads from a MySQL datasource — any MySQL datasource in your Grafana works, whatever it's named. Every dashboard has a **Data Source** selector at the top; pick yours there. See [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how to create the datasource if you don't have one yet.

## Variables

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `outageType` | No — optional filter | All | Restrict to Unplanned/Planned/Exempt. |
| `deviceType` | No — optional filter | All | Restrict to specific device types. |
| `devices` | No — optional filter | All | Restrict to specific devices. |

Note: unlike the Device Availability dashboards, `outageType` here defaults to **All**, not Unplanned-only — Outage Log is meant to be the full ledger.

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | The saved datasource value is a uid from a different Grafana | Pick yours from the **Data Source** selector at the top of the dashboard |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Row-level drill-down link errors | Quiet | `spectrum-device-detail.json` wasn't imported | Import it too — see [Device Detail](spectrum-device-detail.md) |
| Counts differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON.
