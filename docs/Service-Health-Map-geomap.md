# Service Health Map (geo-map) — what it is & how to configure it

## What it is

The **Service Health Map** is a panel on the **Service Availability & Health**
dashboard. It plots Service Manager services on a US map, colored by their
latest health state (green = Up, red = Down / Loss of Management,
orange = Degraded, yellow = Slightly Degraded).

**It is a Grafana enhancement — it is NOT part of the CABI Reports.** There is no
geo-map in the CABI (CA Business Intelligence / Operational Reports) set; this is
an additive capability Grafana provides that the legacy CABI reports did not.
It is optional.

On the dashboard the section is labelled:
> *Service Health Map (optional — click to expand) · Enhancement - not included in CABI*

## How to turn it on (end user)

The map lives in an expandable section at the bottom of the dashboard:

1. Open the **Service Availability & Health** dashboard.
2. Scroll to the bottom section **"Service Health Map (optional — click to
   expand) · Enhancement - not included in CABI"**.
3. **Click the section header** to expand/collapse the map.

While collapsed, the map's query does not run, so there is no extra load.

---

## ⚠️ How to make a service appear on the map (important — this is a workaround)

**Read this before configuring.** Grafana needs a latitude/longitude for each
service to place it on the map. Spectrum Service Manager has **no native
coordinate field**, so this map **re-purposes the service's `Description`
field** to carry the coordinates. That is a deliberate workaround, and it has
consequences you must understand:

- **Whatever you type in a service's Description is read by the map as its
  coordinates.** If you also want to use Description for human-readable notes,
  you can't do both with this approach (see *Proper alternative* below).
- A service appears on the map **only if** its Description contains a valid
  coordinate pair. Services without one still show in every other panel (stats,
  tables) — they're simply not pinned on the map.

### Exactly what to put in the Description field

Set the service's **Description** to its coordinates in this **exact** format:

```
latitude,longitude
```

- **Decimal degrees only** (e.g. `40.7128`), not degrees/minutes/seconds.
- **Latitude first, longitude second**, separated by a single comma.
- **Negative = West or South.** In the continental US longitude is always
  negative (e.g. `-74.0060`).
- **Nothing else in the field** — no labels, no spaces-and-text, no trailing
  notes. The field must contain *only* the two numbers and the comma.

### Worked examples (these are the services currently on the map)

| Service | Put this in Description | Shows up at |
|---|---|---|
| `Tixchange-NewYork` | `40.7128,-74.0060` | New York, NY |
| `Tixchange-Miami` | `25.7617,-80.1918` | Miami, FL |
| `Tixchange-SanFrancisco` | `37.7749,-122.4194` | San Francisco, CA |
| `Tixchange` | `32.7767,-96.7970` | Dallas, TX |
| `MicrosoftService` | `42.3601,-71.0589` | Boston, MA |

### Valid vs invalid

| Description value | Result |
|---|---|
| `40.7128,-74.0060` | ✅ plots in New York |
| `37.7749, -122.4194` | ✅ plots in San Francisco (a space after the comma is OK) |
| `Core router NYC` | ❌ no coordinates → not on map |
| `NYC 40.7128,-74.0060` | ❌ leading text → ignored (must START with the number) |
| `40.7128,-74.0060,HQ` | ❌ trailing text → the part after the last comma (`HQ`) is read as longitude and fails |
| `40°42'46"N 74°00'21"W` | ❌ degrees/minutes/seconds not supported — use decimals |

### Where to set it in Spectrum

1. Open the **OneClick** console.
2. Select the **service model** (the Service Manager service you want to map).
3. In **Component Detail → Information** (Attributes), find the **Description**
   attribute.
4. Enter the coordinate pair exactly as above and **save**.
5. Back in Grafana, expand the map (or refresh) — the service now appears.

### How to find a location's coordinates

In **Google Maps**, right-click the location → the first item in the menu is the
`latitude, longitude` pair → click it to copy, then paste into the Description
(remove the space if you like; a space after the comma is tolerated).

---

## Proper alternative (if Description is needed for real text)

Re-purposing Description is a workaround. The clean long-term option is a
**dedicated coordinate attribute** on the service model (or a separate
landmark/site mapping) that the map query reads instead of Description. If the
client wants this, we can repoint the map's query to that field — the rest of
the panel stays the same. Just let us know the attribute and we'll switch the
source.

## Colors (health mapping)

| Value | Health | Color |
|---|---|---|
| 0 | Up | green |
| 1 | Down | red |
| 2 | Degraded | orange |
| 3 | Slightly Degraded | yellow |
| 5 | Loss of Management | red |

## Summary for the client

> The geo-map is a Grafana enhancement, not a CABI report — none exists in the
> CABI/Operational Reports set. It's optional: expand the **"Service Health Map
> (optional)"** section at the bottom of the Service Availability & Health
> dashboard. To place a service on the map, set that service's **Description**
> field in Spectrum to its coordinates as `latitude,longitude` (e.g.
> `40.7128,-74.0060` for New York) — and *only* that, since the map reads the
> whole Description as coordinates. This re-uses the Description field as a
> workaround; if you need Description for notes instead, we can switch the map to
> a dedicated coordinate attribute.
