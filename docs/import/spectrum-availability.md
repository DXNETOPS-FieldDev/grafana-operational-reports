# Device Availability

*Dashboard files: `spectrum-availability.json` + `spectrum-availability-bizhours.json` · Folder: Availability Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Two dashboards, one page — not because they drill into each other (they don't), but because they're the same availability data viewed two ways, so you'll likely want both.

## What each one shows

- **Device Availability** (`spectrum-availability.json`) — per-device uptime ranking, the classic "least available" report: fleet-availability/outages/devices-affected/downtime tiles, an outages-per-day trend, a downtime chart, and a Top-N least-available table. The headline reliability report.
- **Availability (Business Hours)** (`spectrum-availability-bizhours.json`) — the same idea scored against business hours only, so an overnight maintenance window doesn't tank the number: BH-availability/BH-hours/BH-downtime tiles and a Top-N least-available (BH) table. A fairer score for business-hours-only services.

## How they're linked

They aren't linked to each other. Each links independently to **[Device Detail](spectrum-device-detail.md)** (imported separately — see that page).

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics. This page only covers what's specific to these two dashboards.
2. Import both JSON files, plus `spectrum-device-detail.json` (see **[Device Detail](spectrum-device-detail.md)**) — both dashboards' per-row drill-down needs it.

## Datasource

Both read from a MySQL datasource named **exactly** `Spectrum Reporting` or `Spectrum MySQL` — see [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource).

## Variables

Both dashboards share these six variables:

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | Only if not named `Spectrum Reporting`/`Spectrum MySQL` | *(auto-resolves)* | Which MySQL connection to query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `topN` | No — optional filter | 20 | How many least-available devices to rank. |
| `outageType` | No — optional filter | Unplanned | Which outage types count (Unplanned / Planned / Exempt) — note the default excludes Planned and Exempt, not "All". |
| `deviceType` | No — optional filter | All | Restrict to specific device types. |
| `devices` | No — optional filter | All | Restrict to specific devices. |

Availability (Business Hours) has three additional variables:

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `bizStart` | No — optional filter | 8 | Business-day start hour (24h clock). |
| `bizEnd` | No — optional filter | 17 | Business-day end hour (24h clock). |
| `countWeekends` | No — optional filter | No | Whether weekends count toward the business-hours window. |

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | Datasource variable's saved value is a uid from another Grafana | Load the page once in a browser — `$datasource` re-resolves by name automatically |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Row-level drill-down link errors | Quiet | `spectrum-device-detail.json` wasn't imported | Import it too — see [Device Detail](spectrum-device-detail.md) |
| Fewer outages or less downtime than expected on Device Availability | Quiet | `outageType` defaults to Unplanned only — Planned and Exempt outages are excluded | Add Planned and/or Exempt to `outageType` if you want them counted |
| Availability (Business Hours) looks artificially high | Quiet | `bizStart`/`bizEnd`/`countWeekends` default to an 8–17, weekdays-only window | Adjust `bizStart`, `bizEnd`, and `countWeekends` to match your actual business window |
| Counts differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON.
