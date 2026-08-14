# Event Log & Top-N Events

*Dashboard file: `spectrum-event-log.json` · Folder: Event Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Links out to **[Device Detail](spectrum-device-detail.md)**; nothing links to this page.

## What this shows

Consolidates the raw event stream plus both "Top-N" event views into one dashboard: totals tiles, an events-over-time trend, a Top-N-by-type chart/table, a Top-N-by-device table, and a detailed (latest-200) log. One stop for trend, type-ranking, and device-ranking instead of the equivalent prior reports spread across three separate views.

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics (folders, service-account token, deploy script vs. manual import). This page only covers what's specific to Event Log & Top-N Events.
2. Import `spectrum-event-log.json`, plus `spectrum-device-detail.json` (see **[Device Detail](spectrum-device-detail.md)**) — its row-level drill-down needs it.

## Datasource

Reads from a MySQL datasource. On a stock **Custom Dashboards** install that is named `mysql-spectrum-reporting`; `Spectrum Reporting` and `Spectrum MySQL` are matched too. **If yours is named something else you do not need to rename it** — every dashboard has a **Data Source** selector at the top; pick yours there. See [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how to create the datasource if you don't have one yet.

## Variables

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | Only if your datasource has a different name — pick it from the **Data Source** selector at the top | *(matches `mysql-spectrum-reporting`, `Spectrum Reporting`, `Spectrum MySQL`)* | Which MySQL connection the panels query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `devices` | No — optional filter | All | Restrict to specific devices. |
| `topN` | No — optional filter | 10 | How many event types/devices to rank. |

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | The saved datasource value is a uid from a different Grafana | Pick yours from the **Data Source** selector at the top of the dashboard |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Row-level drill-down link errors | Quiet | `spectrum-device-detail.json` wasn't imported | Import it too — see [Device Detail](spectrum-device-detail.md) |
| Numbers differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON.
