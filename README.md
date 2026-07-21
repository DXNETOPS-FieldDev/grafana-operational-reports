# Grafana Operational Reports

Grafana dashboards migrated from CABI Operational Reports for **DX NetOps Spectrum**.

## Contents

| Folder | Description |
|---|---|
| `dashboards/` | Grafana dashboard JSON files (import directly via Grafana UI or API) |
| `deploy/` | Automated deployment script + folder-tree mapping (see `docs/Deploying-to-a-New-Grafana-Environment.md`) |
| `docs/` | User-facing documentation for individual reports |

## Dashboards

| File | Report Name | Domain |
|---|---|---|
| `spectrum-home.json` | Home (navigation hub) | — |
| `spectrum-alarm-log.json` | Alarm Log | Alarm |
| `spectrum-alarm-activity.json` | Alarm Activity by User | Alarm |
| `spectrum-alarm-count-trend.json` | Alarm Count Trend | Alarm |
| `spectrum-alarm-mttr.json` | Alarm MTTR | Alarm |
| `spectrum-alarm-top-devices.json` | Top Devices by Alarm Count | Alarm |
| `spectrum-top-alarms.json` | Top Most Common Alarms | Alarm |
| `spectrum-alarm-detail.json` | Alarm Detail (drill-down) | Alarm |
| `spectrum-availability.json` | Device Availability | Availability |
| `spectrum-availability-bizhours.json` | Availability During Business Hours | Availability |
| `spectrum-availability-class-vendor.json` | Availability by Class / Vendor | Availability |
| `spectrum-outage-log.json` | Outage Log | Availability |
| `spectrum-service-availability.json` | Service Availability & Health | Service |
| `spectrum-service-summary.json` | Service Summary | Service |
| `spectrum-service-detail.json` | Service Detail (drill-down) | Service |
| `spectrum-current-assets.json` | Current Assets | Asset |
| `spectrum-chassis-assets.json` | Chassis Assets | Asset |
| `spectrum-current-ports.json` | Current Ports | Asset |
| `spectrum-current-ports-capacity.json` | Ports Capacity | Asset |
| `spectrum-assets-customizable.json` | Assets (Customizable) | Asset |
| `spectrum-port-assets-customizable.json` | Port Assets (Customizable) | Asset |
| `spectrum-event-log.json` | Event Log | Event |
| `spectrum-change-management.json` | Change Management | Event |
| `spectrum-device-detail.json` | Device Detail (drill-down) | — |
| `spectrum-customer-detail.json` | Customer Detail (drill-down) | — |

## Deploying to a new environment

See **`docs/Deploying-to-a-New-Grafana-Environment.md`** for the full guide,
including the automated deploy script (`deploy/deploy_dashboards.py`) that
recreates the folder tree and pushes all 25 dashboards in one step.

For a one-off manual import instead:
1. In Grafana, go to **Dashboards → Import**.
2. Upload the JSON file or paste its contents.
3. Select the **Spectrum Reporting** datasource when prompted.

All dashboards use a portable datasource variable that resolves to any MySQL datasource whose name matches `Spectrum Reporting` or `Spectrum MySQL`.

## Datasource

Dashboards query the Spectrum `reporting` schema via MySQL. The datasource must be configured in Grafana pointing to the Spectrum reporting database.

## Documentation

- `docs/Deploying-to-a-New-Grafana-Environment.md` — how to deploy this dashboard set to any Grafana instance
- `docs/Alarm-Cause-Filter-OR-AND.md` — how to use OR/AND in the Alarm Cause filter
- `docs/Grafana-vs-Jasper-Parity-2026-06-25.md` — parity analysis vs CABI Reports
- `docs/Service-Health-Map-geomap.md` — Service Health Map enhancement notes
