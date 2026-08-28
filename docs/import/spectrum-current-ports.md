# Current Ports

*Dashboard files: `spectrum-current-ports.json` + `spectrum-current-ports-capacity.json` · Folder: Asset Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Two dashboards, one page — not because they drill into each other (they don't), but because they're the same port-inventory data sliced two ways, so you'll likely want both.

## What each one shows

- **Current Ports** (`spectrum-current-ports.json`) — port inventory by up/down status: devices/total-ports/up-ports/availability tiles plus summary and detail tables. Connectivity troubleshooting.
- **Current Ports — Capacity & Idle** (`spectrum-current-ports-capacity.json`) — the same port inventory viewed as free vs. consumed capacity: available/unavailable/%-available tiles and an idle-threshold detail table. Capacity planning — which ports are free for new circuits, and which have sat idle long enough to reclaim.

## How they're linked

They aren't linked to each other. Each links independently to **[Device Detail](spectrum-device-detail.md)** (imported separately — see that page).

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics. This page only covers what's specific to these two dashboards.
2. Import both JSON files, plus `spectrum-device-detail.json` (see **[Device Detail](spectrum-device-detail.md)**) — both dashboards' per-row drill-down needs it.

## Datasource

Reads from a MySQL datasource — any MySQL datasource in your Grafana works, whatever it's named. Every dashboard has a **Data Source** selector at the top; pick yours there. See [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how to create the datasource if you don't have one yet.

## Variables

Both dashboards use the same two variables:

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `deviceType` | No — optional filter | All | Restrict to specific device types. |

Current Ports — Capacity & Idle has one additional variable:

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `idleDays` | No — optional filter | 30 | A port counts as "idle" once it's been down this many days. |

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | The saved datasource value is a uid from a different Grafana | Pick yours from the **Data Source** selector at the top of the dashboard |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Row-level drill-down link errors | Quiet | `spectrum-device-detail.json` wasn't imported | Import it too — see [Device Detail](spectrum-device-detail.md) |
| Counts differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON.
