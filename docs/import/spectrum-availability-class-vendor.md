# Availability by Class & Vendor

*Dashboard file: `spectrum-availability-class-vendor.json` · Folder: Availability Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Not linked to or from any other dashboard in this set — this page stands alone.

## What this shows

Rolls availability up by device model class/vendor instead of per-device: an availability-% by class chart plus a table with outage counts. A vendor scorecard view — spot a whole product line underperforming.

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics (folders, service-account token, deploy script vs. manual import). This page only covers what's specific to Availability by Class & Vendor.
2. Import `spectrum-availability-class-vendor.json`.

## Datasource

Reads from a MySQL datasource named **exactly** `Spectrum Reporting` or `Spectrum MySQL` — see [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how the name-based resolution works and how to create the datasource if you don't have one yet.

## Variables

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | Only if your datasource isn't named `Spectrum Reporting`/`Spectrum MySQL` | *(auto-resolves by name)* | Which MySQL connection the panels query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `outageType` | No — optional filter | Unplanned | Which outage types count (Unplanned / Planned / Exempt) — note the default excludes Planned and Exempt, not "All". |
| `deviceType` | No — optional filter | All | Restrict to specific device types. |

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | Datasource variable's saved value is a uid from another Grafana | Load the page once in a browser — `$datasource` re-resolves by name automatically |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Numbers look lower than expected | Quiet | `outageType` defaults to Unplanned only, not All | Add Planned and/or Exempt to the filter if you want the full outage picture |
| Numbers differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON.
