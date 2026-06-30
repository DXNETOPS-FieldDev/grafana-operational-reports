# Grafana ↔ Jasper Parity — Response to Testing Feedback (2026-06-25)

Covers the three reports flagged in *Grafana Reports Testing.pdf* for the
**6/18 12am → 6/19 12am** comparison window.

## TL;DR

Two of the three "mismatches" were **not dashboard bugs** — they were caused by
the Grafana time picker being on a **different 24-hour window** than the Jasper
report (a timezone effect, explained below). When both are pointed at the *same*
window, the numbers match Jasper exactly. The third (Alarm Log) had a small,
genuine query-logic difference that has now been fixed.

| Report | Status | Detail |
|---|---|---|
| **Alarm Activity by User** | ✅ Already correct | At Jasper's window = **400 / 0 / 0 / 0 / 0** — exact match. The 427 was the shifted window. |
| **Top-N Most Common Alarms** | ✅ Already correct | At Jasper's window: total **413**, top type **78** — exact match. |
| **Alarm Log** | ✅ Fixed (v7) | Now matches Jasper's "active-during-window" counting. Total **360**. |

---

## The main cause: time zone of the dashboard time picker

- The reporting database stores all alarm times in **UTC**.
- The Jasper reports use **UTC midnight → UTC midnight** as the day boundary
  (verified: querying that exact window reproduces every Jasper number).
- The Grafana dashboards are set to **Browser time**, meaning the time picker
  shows and accepts times in **your computer's local time zone**.

So if your browser is, say, US Eastern (UTC-4) and you pick "midnight," Grafana
actually queries a window shifted by 4 hours from the one Jasper used — which
pulls in (or drops) alarms near the boundary and makes the totals differ. This
is exactly what produced the "extra" 27 activities in Alarm Activity and the
Top-N differences. The dashboard math was right; the **window was different**.

### How to line Grafana up with Jasper (end-user steps)

You can switch any dashboard's view to UTC yourself — no admin change needed:

1. Click the **time-range** control (top-right of the dashboard).
2. Click **Change time settings**.
3. Set **Time zone → Coordinated Universal Time (UTC)**.
4. Now enter the same window Jasper uses, e.g.
   `2026-06-18 00:00:00` to `2026-06-19 00:00:00`.

With the picker in UTC, the displayed times and the queried window match
Jasper's report period one-for-one, and the counts line up.

> Note: in Browser-time mode the timestamps shown in tables are in *your* local
> zone, so an alarm Jasper lists at `08:09 PM` may display at a different
> clock time for you even though it is the same event. Switching the picker to
> UTC also makes the displayed timestamps match Jasper.

---

## Alarm Log — the one genuine fix (dashboard v7)

Jasper's Alarm Log counts every alarm **active at any point during the window**
(opened before and cleared inside it, opened inside and still open, etc.), and
applies its minimum-duration filter **only to alarms that have cleared**.

Our dashboard previously counted only alarms **opened inside** the window and
applied the duration filter to every alarm. That under-counted long-running
alarms that spanned the boundary.

**Fixed:** the count tiles and the Alarm Log table now use Jasper's
active-during-window logic and cleared-only minimum-duration. Over the
6/18 (UTC) window this yields:

| Tile | Value |
|---|---|
| Total Alarms | **360** |
| Critical | 63 |
| Major | 297 |
| Minor | 0 |
| Devices w/ Alarms | 114 |

(The "Alarms per Day" chart intentionally still buckets by the alarm's *start
day*, so its per-day bars can differ slightly from the active-during-window
total — that is expected for a daily trend chart.)

---

## What was checked, for the record

- `alarm_key` is unique in `alarminfo` (no double-counting from joins).
- Raw `alarmactivity` for UTC 6/18 = 400 cleared, 0 others → matches Jasper.
- Top-N: condition filter makes no difference for this data (all alarms are
  Critical/Major/Minor); total 413 and top type 78 match Jasper.
- All numbers reproduced directly against the reporting database and confirmed
  on the live dashboard.
