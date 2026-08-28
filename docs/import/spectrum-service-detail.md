# Service Detail

*Dashboard files: `spectrum-service-detail.json` + `spectrum-service-availability.json` + `spectrum-customer-detail.json` · Folder: Service/SLA Reports · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Three dashboards, one page — each links into the next, so set them up together.

## What each one shows

- **Service Availability & Health** (`spectrum-service-availability.json`) — rolls device availability up to the *service* layer: total-services/impaired/avg-availability tiles, a worst-performing chart, a service inventory, and an optional **Service Health Map** (expanded by default) plotting each customer site on a map, colored by that customer's worst current health. Hover a pin for two tabs: **Customer Site** (the site's overall health) and **Services** (every service at that site, worst first) — so a red pin's cause is visible without leaving the map. Bridges infrastructure to business impact, and the map turns "which service is hurting" into "is this the service itself, or just a few sites" — if most sites on the map are red, look at the service; if only a few are, look at those sites.
- **Service Detail** (`spectrum-service-detail.json`) — per-service deep-dive, reached from Service Availability & Health: availability/outages/customers/owners for one service, its outage history, and who owns it.
- **Customer Detail** (`spectrum-customer-detail.json`) — per-customer drilldown: contact info and the services that customer uses.

## How they're linked

Service Availability & Health → Service Detail → Customer Detail → back to Service Availability & Health. It's a loop, not a one-way chain — any of the three can be a reasonable entry point.

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics. This page only covers what's specific to these three dashboards.
2. Import all three JSON files together — each one's drill-down depends on the other two existing in your Grafana.

## Datasource

Reads from a MySQL datasource — any MySQL datasource in your Grafana works, whatever it's named. Every dashboard has a **Data Source** selector at the top; pick yours there. See [Step 1 of the deploy guide](../Deploying-to-a-New-Grafana-Environment.md#step-1--verify-the-datasource) for how to create the datasource if you don't have one yet.

## Variables

**Service Availability & Health**

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `service` | No — optional filter | All | Restrict to specific services. |
| `customer` | No — optional filter | All | Restrict to a specific customer's services. |
| `downStates` | No — optional filter | Down | Which states count as "down" (Down / Degraded / Slightly Degraded / Loss Of Management). |
| `topN` | No — optional filter | 10 | How many worst-performing services to rank. |

**Service Detail**

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `service` | **Yes, if opened directly** — arriving via a link sets it for you | *(re-queries your data; no "All")* | Which service this page is about. |

**Customer Detail**

| Variable | Must set before use? | Default | What it does |
|---|---|---|---|
| `datasource` | No — pick it from the **Data Source** selector at the top, whatever it's named | *(any MySQL datasource in your Grafana)* | Which MySQL connection the panels query. |
| `customer` | **Yes, if opened directly** — arriving via a link sets it for you | *(re-queries your data; no "All")* | Which customer this page is about. |
| `downStates` | No — optional filter | Down | Which states count as "down" for that customer's services. |

`service` and `customer` are single-select query variables with no "All" option — opened directly (not via a link), they re-query your own data and land on some record from the list rather than showing nothing, so just confirm it's the one you meant.

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| "Data source not found" right after import | Loud | The saved datasource value is a uid from a different Grafana | Pick yours from the **Data Source** selector at the top of the dashboard |
| Every panel says "No data" | Quiet | Datasource name doesn't match, or wrong database | Confirm **Save & Test** passes and it points at the `reporting` database |
| Service Detail / Customer Detail shows an unexpected record | Quiet | Opened directly rather than via a drill-down link | Pick the right value from the `service`/`customer` dropdown |
| Counts differ from what you expected for a given day | Quiet | Database timestamps are UTC; the dashboard defaults to your browser's local timezone | Check the time range against UTC before assuming a data problem |
| Service Health Map is empty, or only shows some customers | Quiet | A customer only appears on the map if their Primary (or Secondary) Contact Location field is set to `latitude,longitude` — nothing else in the field, decimal degrees, comma-separated | Set that field on the customer record; every other panel on this page is unaffected either way |

## Safe to change by hand

Titles, colors/thresholds, panel size and layout — edit directly in Grafana's panel editor, no need to touch the JSON. Don't rename these dashboards' uids (`spectrum-service-detail`, `spectrum-service-availability`, `spectrum-customer-detail`) if you keep all three — their drill-down links are hardcoded to each other.
