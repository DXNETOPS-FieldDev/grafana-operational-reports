# Alarm Log

*Dashboard files: `spectrum-alarm-log.json` + `spectrum-alarm-detail.json` + `spectrum-top-alarms.json` · Folder: Alarm Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Three dashboards, one page — they drill into each other, so set them up together.

## What each one shows

- **Alarm Log** (`spectrum-alarm-log.json`) — the primary alarm ledger for a time window: severity/device-count stat tiles, an alarms-per-day trend, and a filterable alarm table.
- **Alarm Detail** (`spectrum-alarm-detail.json`) — single-alarm lookup, reached by clicking a row in Alarm Log: full context on one alarm without hunting the log.
- **Top-N Most Common Alarms** (`spectrum-top-alarms.json`) — ranks alarm *types* by frequency rather than listing individual alarms; a noise-reduction/root-cause lens that links into Alarm Log to see the underlying events.

## How they're linked

Top-N Most Common Alarms → Alarm Log → Alarm Detail. Alarm Log also links to **[Device Detail](spectrum-device-detail.md)** (imported separately — see that page).

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics. This page only covers what's specific to these three dashboards.
2. Import all three JSON files, plus `spectrum-device-detail.json` (see **[Device Detail](spectrum-device-detail.md)**) — Alarm Log's per-row drill-down needs it.

## Datasource

Reads from a MySQL datasource — any MySQL datasource in your Grafana works, whatever it's named. Every dashboard has a **Data Source** selector at the top; pick yours there. See [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how to create the datasource if you don't have one yet.

## Variables

**Alarm Log**

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `condition` | No — optional filter | All | Restrict to Critical/Major/Minor/Maintenance. |
| `minDuration` | No — optional filter | 300 (seconds) | Hide short-lived alarms below this duration. |
| `cause` | No — optional filter | `%` (matches everything) | SQL `LIKE` filter on alarm cause text. |
| `devices` | No — optional filter | All | Restrict to specific devices. |

**Alarm Detail**

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `alarmId` | **Yes, if opened directly** — arriving via the Alarm Log link sets it for you | *(blank)* | Which alarm to show. Blank shows nothing. |
| `snowHost` | **Yes** | `your-servicenow-instance.example.com` (placeholder) | Hostname the "Open in ServiceNow" link points at. Set it to your own ServiceNow instance, or the link won't resolve. |

**Top-N Most Common Alarms**

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `group` | No — optional filter | All | Restrict to a device group/collection. |
| `condition` | No — optional filter | All | Restrict to Critical/Major/Minor/Maintenance. |
| `topN` | No — optional filter | 10 | How many alarm types to rank. |

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | The saved datasource value is a uid from a different Grafana | Pick yours from the **Data Source** selector at the top of the dashboard |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Alarm Detail is blank when opened directly | Quiet | `alarmId` is empty — it's a drill-down-only field | Open it via a link from Alarm Log, or set `alarmId` manually |
| "Open in ServiceNow" link goes to the wrong place, or 404s | Cosmetic but real | `snowHost` is still the placeholder value | Set it to your own ServiceNow host |
| Counts differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON. Don't rename these dashboards' uids (`spectrum-alarm-log`, `spectrum-alarm-detail`, `spectrum-top-alarms`) if you keep all three — their drill-down links are hardcoded to each other.
