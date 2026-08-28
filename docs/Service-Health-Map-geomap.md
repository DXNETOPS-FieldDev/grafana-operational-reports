# Service Health Map (geo-map) — what it is & how to configure it

**Rebuilt 2026-08-28** — this panel used to plot *services*, using a hacked
coordinate value in each service's Description field. That approach was
removed 2026-06-30 at the client's request — not a rejection of the map
itself, but of *how* it sourced coordinates. It's back, rebuilt to plot
*customer sites* using a real Spectrum field instead. If you're looking for
the old service-Description approach, it no longer exists; don't re-add it.

## What it is

The **Service Health Map** is a panel on the **Service Availability & Health**
dashboard. It plots **customer sites** on a US map — one pin per customer,
not per service — colored by that customer's worst current health across
whichever services are in scope. It respects the dashboard's existing
**Service** and **Customer** filters, exactly like every other panel here.

**Hover a pin to see why it's that color.** The tooltip has two tabs:

- **Customer Site** (left, shown by default) — the customer name and its
  worst current health, matching the pin's color and the **Current Health**
  wording used in the Service Availability & Health table above (Up /
  Maintenance / Slightly Degraded / Degraded / Down / Loss Of Management).
- **Services** (right) — every service used at that site, each with its own
  health, worst first. This answers the question the map's color alone can't:
  *which* service is dragging this site down. If a site has more than one
  service, they list as an expandable group on this tab.

There's no separate service picker for the map — it uses the same **Service**
dropdown at the top of the dashboard that every other panel on this page
does.

**It is a Grafana enhancement — it is NOT part of the CABI Reports.** There is
no geo-map in the CABI (CA Business Intelligence / Operational Reports) set;
this is an additive capability Grafana provides that the legacy CABI reports
did not.

On the dashboard the section is labelled:
> *Service Health Map (optional) · Enhancement - not included in CABI*

It's expanded by default — no click needed to see it. ("Optional" describes
that it's a Grafana-only addition with no CABI equivalent, not that it's
hidden.)

## Why customer sites, not services

A service can be used by several customers in several places — the motivating
example: one shared app used by ten customer locations, four of which are
having trouble. A per-*service* pin can't show that; it collapses ten sites
into one dot. A per-*customer* pin can, and it also gives a diagnostic read
for free:

- **Most or all of a service's customer-sites are red** → look at the service
  itself — this points at a shared/central cause.
- **A handful of sites are red, most are fine** → look at those specific
  sites — this points at something local to them, not the shared service.

Filter the dashboard's **Service** variable to one service and the map
narrows to just that service's customer footprint, making this read
immediate.

**Known gotcha with this demo's data:** if a service has been split into
several site-specific stand-ins (this environment has `Tixchange`,
`Tixchange-Miami`, `Tixchange-NewYork`, `Tixchange-SanFrancisco` as four
separate service objects, each tied to at most one customer), filtering to
the general/umbrella name alone may show far fewer — or zero — sites than you
expect, because the customer associations live on the site-specific objects,
not the umbrella one. Check **Service Detail → Customers Using This Service**
for the service you're filtering to before concluding the map is wrong.

---

## How a customer site appears on the map

Coordinates come from the **Customer**'s own **Primary Contact Location**
field (falling back to **Secondary Contact Location** if Primary is empty).
This is a real, existing Spectrum Service Manager attribute — nothing is
hacked onto an unrelated field this time. A customer with neither field
populated simply doesn't appear on the map; every other panel on the
dashboard is unaffected.

### Exactly what to put in the field

Set the customer's **Primary Contact Location** (or **Secondary**) to its
coordinates in this **exact** format:

```
latitude,longitude
```

- **Decimal degrees only** (e.g. `40.7128`), not degrees/minutes/seconds.
- **Latitude first, longitude second**, separated by a single comma.
- **Negative = West or South.** In the continental US longitude is always
  negative (e.g. `-74.0060`).
- **Nothing else in the field** — no labels, no trailing notes. A space
  immediately after the comma is fine; anything else in the field is not.

### Worked examples (the three real customers currently on the map)

| Customer | Primary Contact Location | Shows up at |
|---|---|---|
| `Miami-Users` | `25.7617,-80.1918` | Miami, FL |
| `NewYork-Users` | `40.7128,-74.0060` | New York, NY |
| `SanFrancisco-Users` | `37.7749,-122.4194` | San Francisco, CA |

### Valid vs invalid

| Field value | Result |
|---|---|
| `25.7617,-80.1918` | ✅ plots in Miami |
| `37.7749, -122.4194` | ✅ plots in San Francisco (a space after the comma is OK) |
| `Miami office` | ❌ no coordinates → not on map |
| `HQ 25.7617,-80.1918` | ❌ leading text → ignored (must START with the number) |
| `25.7617,-80.1918,HQ` | ❌ trailing text → the part after the last comma (`HQ`) is read as longitude and fails |
| `25°45'42"N 80°11'30"W` | ❌ degrees/minutes/seconds not supported — use decimals |

### Where to set it in Spectrum

1. Open the **OneClick** console.
2. Navigate to **Customers** and select the **SM_Customer** you want to map
   (e.g. `Miami-Users`).
3. In **Component Detail → Information → Contact Information**, find
   **Primary Contact Location** (or **Secondary Contact Location**).
4. Enter the coordinate pair exactly as above and **save**.
5. Back in Grafana, refresh the dashboard — the customer now appears.

### How to find a location's coordinates

In **Google Maps**, right-click the location → the first item in the menu is
the `latitude, longitude` pair → click it to copy, then paste into the field
(a trailing space after the comma is tolerated).

---

## Colors (health mapping)

The map colors each customer by the **worst** health status among their
in-scope services (Up is best, Down/Loss of Management tied for worst):

| Health | Color |
|---|---|
| Up | green |
| Maintenance | blue |
| Slightly Degraded | yellow |
| Degraded | orange |
| Down | red |
| Loss Of Management | red |

## History

- **Original version**: one pin per service, coordinates hacked into the
  service's `Description` field. Removed 2026-06-30 ("Remove geo-map section
  (client request)") because of that mechanism, not the map itself.
- **Current version** (2026-08-28): one pin per customer site, coordinates
  read from the Customer's own Primary/Secondary Contact Location field, and
  scoped by the dashboard's existing Service/Customer filters. Query joins
  `sm_customers` → `sm_customermhs` → `sm_slmuses` → `sm_monitors`, the same
  customer↔service link every other panel on this dashboard already uses.
- **Reviewer refinement pass** (2026-08-28, same day): first review round
  flagged the legend as reading like a raw impact count rather than the same
  health vocabulary as the **Current Health** column above it — fixed by
  mapping the pin color to that same Up/Maintenance/Slightly
  Degraded/Degraded/Down enum. Second round asked to see which service is
  behind a red pin without leaving the map — added the **Services** tab
  described above, sorted worst-to-best, to the right of **Customer Site**.
