# Current Assets (Detailed / Customizable)

*Dashboard files: `spectrum-assets-customizable.json` + `spectrum-chassis-assets.json` · Folder: Asset Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Two dashboards, one page — not because they drill into each other (they don't), but because they're companion inventory views on the same topic, so you'll likely want both.

## What each one shows

- **Current Assets (Detailed / Customizable)** (`spectrum-assets-customizable.json`) — a wide, sortable inventory for ad-hoc digging: a total-assets tile plus a sortable 14-column table. Power-user lookup without needing a bespoke report.
- **Current Chassis-based Assets** (`spectrum-chassis-assets.json`) — inventory scoped to chassis/modular gear (blades, line cards): chassis-modules/devices tiles, a by-vendor pie, and a modules table. Slot/module capacity and vendor-mix tracking, separate from flat asset counts.

## How they're linked

They aren't linked to each other. Each links independently to **[Device Detail](spectrum-device-detail.md)** (imported separately — see that page).

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics. This page only covers what's specific to these two dashboards.
2. Import both JSON files, plus `spectrum-device-detail.json` (see **[Device Detail](spectrum-device-detail.md)**) — both dashboards' drill-down links need it.

## Datasource

Reads from a MySQL datasource — any MySQL datasource in your Grafana works, whatever it's named. Every dashboard has a **Data Source** selector at the top; pick yours there. See [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how to create the datasource if you don't have one yet.

## Variables

Both dashboards use the same two variables:

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `devices` | No — optional filter | All | Restrict to specific devices. |

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | The saved datasource value is a uid from a different Grafana | Pick yours from the **Data Source** selector at the top of the dashboard |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Row-level drill-down link errors | Quiet | `spectrum-device-detail.json` wasn't imported | Import it too — see [Device Detail](spectrum-device-detail.md) |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON.
