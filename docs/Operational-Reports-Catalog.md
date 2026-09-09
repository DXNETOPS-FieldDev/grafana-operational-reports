# Operational Reports — Dashboard Catalog

25 Grafana dashboards migrated from CA Spectrum / DX NetOps CABI-JasperReports, live on Dev Grafana under the **Operational Reports** folder tree. For each dashboard: purpose, what it conveys, and its value.

## Root (Operational Reports)

<a id="spectrum-home"></a>
**Operational Reports — Home**

![Operational Reports — Home dashboard screenshot](screenshots/spectrum-home.png)

Purpose: landing/navigation page for the whole capability. Conveys: a dashlist linking out to every other report. Value: one entry point instead of remembering folder paths — mirrors Jasper's report launcher.

<a id="spectrum-device-detail"></a>
**Device Detail** *(drilldown)*

![Device Detail dashboard screenshot](screenshots/spectrum-device-detail.png)

Purpose: per-device deep-dive, reached by clicking a device from Availability, Outage Log, Alarm Log, or Current Ports. Conveys: asset info, Availability/Outages/Alarms stat tiles, outage list, alarm list, availability & outage-type pie charts. Value: goes from "this device looks bad on a summary" to "here's everything about it" in one click — consolidates several scattered Jasper sub-reports.

## Alarm Reports (7)

<a id="spectrum-alarm-log"></a>
1. **Alarm Log**

![Alarm Log dashboard screenshot](screenshots/spectrum-alarm-log.png)

Purpose: the primary alarm ledger for a time window. Conveys: Total/Critical/Major/Minor/Devices-w-alarms tiles, alarms-per-day trend, filterable alarm table (condition + min-duration), drills to Alarm Detail. Value: first stop for "what alarmed and how bad" — one dashboard replaces Jasper's All/Group/Selected trio.

<a id="spectrum-alarm-activity"></a>
2. **Alarm Activity by User**

![Alarm Activity by User dashboard screenshot](screenshots/spectrum-alarm-activity.png)

Purpose: tracks operator response — who ack'd/cleared/assigned alarms. Conveys: Cleared/Acknowledged/Assigned-By/Assigned-To/Ticketed/Total tiles, Top-Users bar chart, per-user table. Value: NOC accountability/workload view — staffing and process audits.

<a id="spectrum-alarm-mttr"></a>
3. **Alarm Mean Time to Respond**

![Alarm Mean Time to Respond dashboard screenshot](screenshots/spectrum-alarm-mttr.png)

Purpose: how fast the team reacts, by severity. Conveys: count/cleared/ongoing/avg-time-to-first-action tiles, MTTR-by-severity chart, summary + per-alarm detail. Value: process-health metric — are criticals getting acknowledged fast enough (exceeds Jasper by adding per-alarm detail alongside the summary).

<a id="spectrum-alarm-count-trend"></a>
4. **Alarm Count Trend**

![Alarm Count Trend dashboard screenshot](screenshots/spectrum-alarm-count-trend.png)

Purpose: alarm volume over time by severity. Conveys: Total/Critical/Major tiles, severity-stacked trend, window-total chart, per-bucket detail table. Value: spot a rising trend or a "storm" concentrated in one severity/window.

<a id="spectrum-top-alarms"></a>
5. **Top-N Most Common Alarms**

![Top-N Most Common Alarms dashboard screenshot](screenshots/spectrum-top-alarms.png)

Purpose: ranks alarm *types* by frequency. Conveys: bar chart + table, % of total, frequency/day, severity color. Value: noise-reduction/root-cause lens — recurring types are candidates for automation or threshold tuning.

<a id="spectrum-alarm-top-devices"></a>
6. **Top-N Devices & Models with Most Alarms**

![Top-N Devices & Models with Most Alarms dashboard screenshot](screenshots/spectrum-alarm-top-devices.png)

Purpose: ranks *devices/models* by alarm volume. Conveys: totals tiles + ranked bar chart/table with % of total, frequency/day. Value: prioritization list for the flakiest hardware — replacement/firmware/config candidates.

<a id="spectrum-alarm-detail"></a>
7. **Alarm Detail** *(drilldown)*

![Alarm Detail dashboard screenshot](screenshots/spectrum-alarm-detail.png)

Purpose: single-alarm lookup from a Log row. Conveys: one-row detail table. Value: full context on one alarm without hunting the log — the "zoom in" complement to Alarm Log.

## Asset Reports (7)

<a id="spectrum-current-assets"></a>
1. **Current Assets**

![Current Assets dashboard screenshot](screenshots/spectrum-current-assets.png)

Purpose: fleet inventory snapshot by class/vendor. Conveys: Managed-assets/classes/vendors tiles, by-class pie, current-assets-by-class table. Value: baseline "what do we have" view for capacity planning and audits.

<a id="spectrum-assets-customizable"></a>
2. **Current Assets (Detailed / Customizable)**

![Current Assets (Detailed / Customizable) dashboard screenshot](screenshots/spectrum-assets-customizable.png)

Purpose: wide, sortable inventory for ad-hoc digging. Conveys: total-assets tile + sortable 14-column table. Value: power-user lookup without a bespoke report.

<a id="spectrum-chassis-assets"></a>
3. **Current Chassis-based Assets**

![Current Chassis-based Assets dashboard screenshot](screenshots/spectrum-chassis-assets.png)

Purpose: inventory scoped to chassis/modular gear (blades, line cards). Conveys: chassis-modules/devices tiles, by-vendor pie, modules table. Value: slot/module capacity and vendor-mix tracking, separate from flat assets.

<a id="spectrum-current-ports-capacity"></a>
4. **Current Ports — Capacity & Idle**

![Current Ports — Capacity & Idle dashboard screenshot](screenshots/spectrum-current-ports-capacity.png)

Purpose: port utilization — free vs. consumed capacity. Conveys: managed-assets/total-ports/available/unavailable/%-available tiles, by-device summary, idle-threshold detail table. Value: capacity planning — free ports for new circuits, flags long-idle ports to reclaim (cleaner lens than the Jasper original had).

<a id="spectrum-current-ports"></a>
5. **Current Ports** *(link-health)*

![Current Ports dashboard screenshot](screenshots/spectrum-current-ports.png)

Purpose: port inventory by up/down status rather than idle capacity. Conveys: devices/total-ports/up-ports/availability tiles, summary + detail table. Value: connectivity troubleshooting, complementing the Capacity & Idle view.

<a id="spectrum-port-assets-customizable"></a>
6. **Current Port Assets (Customizable)**

![Current Port Assets (Customizable) dashboard screenshot](screenshots/spectrum-port-assets-customizable.png)

Purpose: sortable wide port-asset table (port-level equivalent of #2). Conveys: total-ports/ports-up tiles + sortable table. Value: ad-hoc port inventory lookup.

<a id="spectrum-change-management"></a>
7. **Detailed Change Management**

![Detailed Change Management dashboard screenshot](screenshots/spectrum-change-management.png)

Purpose: device lifecycle churn — additions/removals in a range. Conveys: devices-added/removed tiles + change-log table. Value: audit trail for change-control review, catches unexpected adds/removals.

## Availability Reports (4)

<a id="spectrum-availability"></a>
1. **Device Availability**

![Device Availability dashboard screenshot](screenshots/spectrum-availability.png)

Purpose: per-device uptime ranking, the classic "least available" report. Conveys: fleet-availability/outages/devices-affected/downtime tiles, outages-per-day trend, downtime chart, Top-N least-available table. Value: headline reliability report, drills to Device Detail for root cause.

<a id="spectrum-outage-log"></a>
2. **Outage Log**

![Outage Log dashboard screenshot](screenshots/spectrum-outage-log.png)

Purpose: raw outage ledger, planned or not. Conveys: total/unplanned/planned/exempt/devices-w-outage tiles, outage table with an "ongoing" label. Value: source-of-truth event list behind the availability numbers — needed for RCA.

<a id="spectrum-avail-class-vendor"></a>
3. **Availability by Class & Vendor**

![Availability by Class & Vendor dashboard screenshot](screenshots/spectrum-avail-class-vendor.png)

Purpose: rolls availability up by model class/vendor instead of per-device. Conveys: availability-% by class chart + table with outage counts. Value: vendor scorecards — spot a whole product line underperforming.

<a id="spectrum-avail-bizhours"></a>
4. **Availability (Business Hours)**

![Availability (Business Hours) dashboard screenshot](screenshots/spectrum-avail-bizhours.png)

Purpose: availability against business hours only *(Grafana-only addition, no Jasper equivalent)*. Conveys: BH-availability/BH-hours/BH-downtime tiles, Top-N least-available (BH) table. Value: fairer score for business-hours-only services — an overnight maintenance window doesn't tank it.

## Event Reports (1)

<a id="spectrum-event-log"></a>
**Event Log & Top-N Events**

![Event Log & Top-N Events dashboard screenshot](screenshots/spectrum-event-log.png)

Purpose: consolidates the raw event stream plus both Jasper "Top-N" event reports into one dashboard. Conveys: totals tiles, events-over-time trend, Top-N-by-type chart/table, Top-N-by-device table, detailed (latest-200) log. Value: one stop for trend + type-ranking + device-ranking instead of three separate Jasper reports.

## Service/SLA Reports (4)

<a id="spectrum-service-availability"></a>
1. **Service Availability & Health**

![Service Availability & Health dashboard screenshot](screenshots/spectrum-service-availability.png)

Purpose: rolls device availability up to the *service* layer. Conveys: total-services/impaired/avg-availability tiles, Top-N worst-performing chart, health table, service-inventory (services → resources), and an optional **Service Health Map** — a geo-map plotting each customer site, colored by its worst current health, letting you see at a glance whether a problem is one shared service (most sites affected) or a handful of local sites. Value: bridges infrastructure to business impact — "which customer-facing service is hurting," not just "which router is down" — and the map turns that into "is this the app, or is it these specific sites."

<a id="spectrum-customer-detail"></a>
2. **Customer Detail**

![Customer Detail dashboard screenshot](screenshots/spectrum-customer-detail.png)

Purpose: per-customer drilldown — contact info + services used. Conveys: services-used tile, contact table, services-by-customer table. Value: account-management view — a customer's footprint and the right contact, fast.

<a id="spectrum-service-detail"></a>
3. **Service Detail** *(drilldown)*

![Service Detail dashboard screenshot](screenshots/spectrum-service-detail.png)

Purpose: per-service deep-dive from Service Availability & Health. Conveys: service info, availability/outages/customers/owners tiles, outage-details table, customers-using-this-service table, owners table. Value: ties a service to its outage history, affected customers, and owner — "who do I call, what broke."

<a id="spectrum-service-summary"></a>
4. **Service Summary & Inventory**

![Service Summary & Inventory dashboard screenshot](screenshots/spectrum-service-summary.png)

Purpose: rolls up availability against a target %, by service and by customer, plus resource inventory. Conveys: total-services/avg-%/below-target tiles, two target-scored tables, resource inventory table. Value: SLA-adjacent scorecard (since true SLA data doesn't exist in this source) — flags services missing target.

## Known gap (deliberate, not an oversight)

The 6 true SLA reports (SLA Detail/Summary/Status/Inventory by SLA or Customer) were **not** migrated — `sm_slaperiods`/`sm_guaranteeperiods` are empty because the SLA engine was never run in this environment, confirmed against the live SQL, not assumed. Same story for **Alarm Noise Reduction** — that's an AIOps/correlation-layer output, not something the Spectrum reporting schema has. If asked "where's the SLA report," that's the answer — no source data, not a bug.
