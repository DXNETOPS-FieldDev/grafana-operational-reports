# Grafana Operational Reports

Grafana dashboards migrated from CABI Operational Reports for **DX NetOps Spectrum**.

## Contents

| Folder | Description |
|---|---|
| `dashboards/` | Grafana dashboard JSON files (import directly via Grafana UI or API) |
| `deploy/` | Automated deployment script + folder-tree mapping (see `docs/Deploying-to-a-New-Grafana-Environment.md`) |
| `docs/` | User-facing documentation for individual reports |

## Dashboards

| File | Report Name | Domain | Import Doc |
|---|---|---|---|
| `spectrum-home.json` | Home (navigation hub) | — | [Guide](docs/import/spectrum-home.md) |
| `spectrum-alarm-log.json` | Alarm Log | Alarm | [Guide](docs/import/spectrum-alarm-log.md) |
| `spectrum-alarm-activity.json` | Alarm Activity by User | Alarm | [Guide](docs/import/spectrum-alarm-activity.md) |
| `spectrum-alarm-count-trend.json` | Alarm Count Trend | Alarm | [Guide](docs/import/spectrum-alarm-count-trend.md) |
| `spectrum-alarm-mttr.json` | Alarm MTTR | Alarm | [Guide](docs/import/spectrum-alarm-mttr.md) |
| `spectrum-alarm-top-devices.json` | Top Devices by Alarm Count | Alarm | [Guide](docs/import/spectrum-alarm-top-devices.md) |
| `spectrum-top-alarms.json` | Top Most Common Alarms | Alarm | [Guide](docs/import/spectrum-alarm-log.md) |
| `spectrum-alarm-detail.json` | Alarm Detail (drill-down) | Alarm | [Guide](docs/import/spectrum-alarm-log.md) |
| `spectrum-availability.json` | Device Availability | Availability | [Guide](docs/import/spectrum-availability.md) |
| `spectrum-availability-bizhours.json` | Availability During Business Hours | Availability | [Guide](docs/import/spectrum-availability.md) |
| `spectrum-availability-class-vendor.json` | Availability by Class / Vendor | Availability | [Guide](docs/import/spectrum-availability-class-vendor.md) |
| `spectrum-outage-log.json` | Outage Log | Availability | [Guide](docs/import/spectrum-outage-log.md) |
| `spectrum-service-availability.json` | Service Availability & Health | Service | [Guide](docs/import/spectrum-service-detail.md) |
| `spectrum-service-summary.json` | Service Summary | Service | [Guide](docs/import/spectrum-service-summary.md) |
| `spectrum-service-detail.json` | Service Detail (drill-down) | Service | [Guide](docs/import/spectrum-service-detail.md) |
| `spectrum-current-assets.json` | Current Assets | Asset | [Guide](docs/import/spectrum-current-assets.md) |
| `spectrum-chassis-assets.json` | Chassis Assets | Asset | [Guide](docs/import/spectrum-assets-customizable.md) |
| `spectrum-current-ports.json` | Current Ports | Asset | [Guide](docs/import/spectrum-current-ports.md) |
| `spectrum-current-ports-capacity.json` | Ports Capacity | Asset | [Guide](docs/import/spectrum-current-ports.md) |
| `spectrum-assets-customizable.json` | Assets (Customizable) | Asset | [Guide](docs/import/spectrum-assets-customizable.md) |
| `spectrum-port-assets-customizable.json` | Port Assets (Customizable) | Asset | [Guide](docs/import/spectrum-port-assets-customizable.md) |
| `spectrum-event-log.json` | Event Log | Event | [Guide](docs/import/spectrum-event-log.md) |
| `spectrum-change-management.json` | Change Management | Event | [Guide](docs/import/spectrum-change-management.md) |
| `spectrum-device-detail.json` | Device Detail (drill-down) | — | [Guide](docs/import/spectrum-device-detail.md) |
| `spectrum-customer-detail.json` | Customer Detail (drill-down) | — | [Guide](docs/import/spectrum-service-detail.md) |

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
