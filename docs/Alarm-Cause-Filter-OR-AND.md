# Alarm Log — "Alarm Cause (filter)" now supports OR / AND

The **Alarm Cause (filter)** box on the **Alarm Log** dashboard now understands
the words **`or`** and **`and`**, so you can match on multiple alarm-cause terms
in one filter.

## How to use it

| What you type | What it matches |
|---|---|
| *(blank)* or `%` | All alarms (no cause filter) |
| `CDP` | Causes containing **CDP** (substring) |
| `CDP or DEVICE` | Causes containing **CDP** *or* **DEVICE** (either) |
| `CDP and DUPLEX` | Causes containing **CDP** *and* **DUPLEX** (both) |
| `LSP or BGP or OSPF` | Any of the three (up to 4 terms) |

- **Case-insensitive** — `cdp`, `CDP`, `Cdp` all work, and so do `OR` / `AND`.
- **Substring match** — `CDP` finds `%CDP-4-DUPLEX_MISMATCH…` (no wildcards
  needed).
- The operator is the **whole word** `or` / `and` surrounded by spaces, so a
  cause that merely *contains* the letters "and" (e.g. `…command…`) is not
  treated as an operator.

## Notes / limits

- Up to **4 terms** per filter (e.g. `a or b or c or d`).
- Use **either** `or` **or** `and` in a single filter — don't mix them in one
  expression (e.g. avoid `A and B or C`).
- Hover the **ⓘ** on the filter label for a built-in reminder of the syntax.

## How it works (for the team)

Implemented purely with `LIKE` + `SUBSTRING_INDEX` term-splitting in each panel
query — **no regex** — so it is safe against alarm titles that contain regex
metacharacters (≈99% of titles do) and does **not** break the Top-N → Alarm Log
drill-down, which passes a full alarm title into this same filter. Verified
against the live database: `CDP or DEVICE` = exact union of `CDP` + `DEVICE`;
`CDP and DEVICE` = 0; full-title drill-down still resolves. Applies to all Alarm
Log panels (5 stat tiles, the per-day chart, and the Alarm Log table).
