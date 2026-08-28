# Service Summary & Inventory

*Dashboard file: `spectrum-service-summary.json` · Folder: Service/SLA Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Not linked to or from any other dashboard in this set — this page stands alone.

## What this shows

Rolls up availability against a target percentage, by service and by customer, plus a resource inventory. Total-services/avg-%/below-target tiles, two target-scored tables, and a resource-inventory table — an SLA-adjacent scorecard that flags services missing their target.

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics (folders, service-account token, deploy script vs. manual import). This page only covers what's specific to Service Summary & Inventory.
2. Import `spectrum-service-summary.json`.

## Datasource

Reads from a MySQL datasource — any MySQL datasource in your Grafana works, whatever it's named. Every dashboard has a **Data Source** selector at the top; pick yours there. See [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how to create the datasource if you don't have one yet.

## Variables

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `reportTitle` | No — cosmetic only | "Summary of Service Availability" | Free-text heading shown on the report; change it to whatever title you want displayed. |
| `service` | No — optional filter | All | Restrict to specific services. |
| `customer` | No — optional filter | All | Restrict to a specific customer's services. |
| `downStates` | No — optional filter | Down | Which states count as "down" (Down / Degraded / Slightly Degraded / Loss Of Management). |
| `availTarget` | **Yes — this drives the whole scorecard** | 99 | The availability percentage (e.g. 99, 99.9) every service/customer is scored against. Set this to your actual SLA target before treating the "below target" tiles as meaningful — the default of 99 is just an example, not a real commitment. |

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | The saved datasource value is a uid from a different Grafana | Pick yours from the **Data Source** selector at the top of the dashboard |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Numbers differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |
| "Below target" tiles flag services that seem fine | Quiet | `availTarget` was left at its default of 99 instead of your actual SLA target | Set `availTarget` to the percentage you actually commit to before trusting the scorecard |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON.
