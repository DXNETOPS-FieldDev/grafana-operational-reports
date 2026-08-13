# Alarm Count Trend

*Dashboard file: `spectrum-alarm-count-trend.json` · Folder: Alarm Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Not linked to or from any other dashboard in this set — this page stands alone.

## What this shows

Alarm volume over time, broken out by severity. Total/Critical/Major tiles, a severity-stacked trend chart, a window-total chart, and a per-bucket detail table. Useful for spotting a rising trend or a "storm" concentrated in one severity or time window.

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics (folders, service-account token, deploy script vs. manual import). This page only covers what's specific to Alarm Count Trend.
2. Import `spectrum-alarm-count-trend.json`.

## Datasource

Reads from a MySQL datasource named **exactly** `Spectrum Reporting` or `Spectrum MySQL` — see [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how the name-based resolution works and how to create the datasource if you don't have one yet.

## Variables

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | Only if your datasource isn't named `Spectrum Reporting`/`Spectrum MySQL` | *(auto-resolves by name)* | Which MySQL connection the panels query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `devices` | No — optional filter | All | Restrict to specific devices. |
| `condition` | No — optional filter | All | Restrict to Critical/Major/Minor/Maintenance. |
| `bucket` | No — optional filter | Daily | Trend bucket size: Hourly, Daily, or Weekly. |

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | Datasource variable's saved value is a uid from another Grafana | Load the page once in a browser — `$datasource` re-resolves by name automatically |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Numbers differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON.
