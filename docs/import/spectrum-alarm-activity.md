# Alarm Activity by User

*Dashboard file: `spectrum-alarm-activity.json` · Folder: Alarm Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Not linked to or from any other dashboard in this set — this page stands alone.

## What this shows

Tracks operator response to alarms: who acknowledged, cleared, or assigned them. Cleared/Acknowledged/Assigned-By/Assigned-To/Ticketed/Total tiles, a top-users bar chart, and a per-user detail table. A NOC accountability and workload view, useful for staffing and process audits.

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics (folders, service-account token, deploy script vs. manual import). This page only covers what's specific to Alarm Activity by User.
2. Import `spectrum-alarm-activity.json`.

## Datasource

Reads from a MySQL datasource. On a stock **Custom Dashboards** install that is named `mysql-spectrum-reporting`; `Spectrum Reporting` and `Spectrum MySQL` are matched too. **If yours is named something else you do not need to rename it** — every dashboard has a **Data Source** selector at the top; pick yours there. See [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how to create the datasource if you don't have one yet.

## Variables

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | Only if your datasource has a different name — pick it from the **Data Source** selector at the top | *(matches `mysql-spectrum-reporting`, `Spectrum Reporting`, `Spectrum MySQL`)* | Which MySQL connection the panels query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `devices` | No — optional filter | All | Restrict to specific devices. |

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | The saved datasource value is a uid from a different Grafana | Pick yours from the **Data Source** selector at the top of the dashboard |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Numbers differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON.
