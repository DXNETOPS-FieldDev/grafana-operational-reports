# Grafana Operational Reports

Grafana dashboards migrated from CABI Operational Reports for **DX NetOps Spectrum**.

## Contents

| Folder | Description |
|---|---|
| `dashboards/` | Grafana dashboard JSON files (import directly via Grafana UI or API) |
| `deploy/` | Automated deployment script + folder-tree mapping (see `docs/Deploying-to-a-New-Grafana-Environment.md`) |
| `docs/` | User-facing documentation for individual reports |

## Dashboards

See [`docs/Operational-Reports-Catalog.md`](docs/Operational-Reports-Catalog.md) for a description **and screenshot** of every dashboard below.

| Report Name | Domain | Screenshot | Import Doc |
|---|---|---|---|
| Home (navigation hub) | — | [View](docs/Operational-Reports-Catalog.md#spectrum-home) | [Guide](docs/import/spectrum-home.md) |
| Alarm Log | Alarm | [View](docs/Operational-Reports-Catalog.md#spectrum-alarm-log) | [Guide](docs/import/spectrum-alarm-log.md) |
| Alarm Activity by User | Alarm | [View](docs/Operational-Reports-Catalog.md#spectrum-alarm-activity) | [Guide](docs/import/spectrum-alarm-activity.md) |
| Alarm Count Trend | Alarm | [View](docs/Operational-Reports-Catalog.md#spectrum-alarm-count-trend) | [Guide](docs/import/spectrum-alarm-count-trend.md) |
| Alarm MTTR | Alarm | [View](docs/Operational-Reports-Catalog.md#spectrum-alarm-mttr) | [Guide](docs/import/spectrum-alarm-mttr.md) |
| Top Devices by Alarm Count | Alarm | [View](docs/Operational-Reports-Catalog.md#spectrum-alarm-top-devices) | [Guide](docs/import/spectrum-alarm-top-devices.md) |
| Top Most Common Alarms | Alarm | [View](docs/Operational-Reports-Catalog.md#spectrum-top-alarms) | [Guide](docs/import/spectrum-alarm-log.md) |
| Alarm Detail (drill-down) | Alarm | [View](docs/Operational-Reports-Catalog.md#spectrum-alarm-detail) | [Guide](docs/import/spectrum-alarm-log.md) |
| Device Availability | Availability | [View](docs/Operational-Reports-Catalog.md#spectrum-availability) | [Guide](docs/import/spectrum-availability.md) |
| Availability During Business Hours | Availability | [View](docs/Operational-Reports-Catalog.md#spectrum-avail-bizhours) | [Guide](docs/import/spectrum-availability.md) |
| Availability by Class / Vendor | Availability | [View](docs/Operational-Reports-Catalog.md#spectrum-avail-class-vendor) | [Guide](docs/import/spectrum-availability-class-vendor.md) |
| Outage Log | Availability | [View](docs/Operational-Reports-Catalog.md#spectrum-outage-log) | [Guide](docs/import/spectrum-outage-log.md) |
| Service Availability & Health | Service | [View](docs/Operational-Reports-Catalog.md#spectrum-service-availability) | [Guide](docs/import/spectrum-service-detail.md) |
| Service Summary | Service | [View](docs/Operational-Reports-Catalog.md#spectrum-service-summary) | [Guide](docs/import/spectrum-service-summary.md) |
| Service Detail (drill-down) | Service | [View](docs/Operational-Reports-Catalog.md#spectrum-service-detail) | [Guide](docs/import/spectrum-service-detail.md) |
| Current Assets | Asset | [View](docs/Operational-Reports-Catalog.md#spectrum-current-assets) | [Guide](docs/import/spectrum-current-assets.md) |
| Chassis Assets | Asset | [View](docs/Operational-Reports-Catalog.md#spectrum-chassis-assets) | [Guide](docs/import/spectrum-assets-customizable.md) |
| Current Ports | Asset | [View](docs/Operational-Reports-Catalog.md#spectrum-current-ports) | [Guide](docs/import/spectrum-current-ports.md) |
| Ports Capacity | Asset | [View](docs/Operational-Reports-Catalog.md#spectrum-current-ports-capacity) | [Guide](docs/import/spectrum-current-ports.md) |
| Assets (Customizable) | Asset | [View](docs/Operational-Reports-Catalog.md#spectrum-assets-customizable) | [Guide](docs/import/spectrum-assets-customizable.md) |
| Port Assets (Customizable) | Asset | [View](docs/Operational-Reports-Catalog.md#spectrum-port-assets-customizable) | [Guide](docs/import/spectrum-port-assets-customizable.md) |
| Event Log | Event | [View](docs/Operational-Reports-Catalog.md#spectrum-event-log) | [Guide](docs/import/spectrum-event-log.md) |
| Change Management | Event | [View](docs/Operational-Reports-Catalog.md#spectrum-change-management) | [Guide](docs/import/spectrum-change-management.md) |
| Device Detail (drill-down) | — | [View](docs/Operational-Reports-Catalog.md#spectrum-device-detail) | [Guide](docs/import/spectrum-device-detail.md) |
| Customer Detail (drill-down) | — | [View](docs/Operational-Reports-Catalog.md#spectrum-customer-detail) | [Guide](docs/import/spectrum-service-detail.md) |

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
