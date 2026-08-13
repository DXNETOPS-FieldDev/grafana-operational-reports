# Operational Reports — Home

*Dashboard file: `spectrum-home.json` · Folder: root · [Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)*

Not linked to or from any other dashboard by drill-down — it links to everything by a different mechanism (see below).

## What this shows

A landing/navigation page for the whole set: a list panel linking out to every other report. One entry point instead of remembering folder paths.

## How this one's different

Every other page in this set is a data dashboard with variables to configure. Home has no queries and no variables — it's a single dashboard-list panel that finds other dashboards **by tag**, not by a fixed link list. It lists anything tagged `operational-reports`, up to 30 dashboards.

That means: **the list only shows what you've imported and tagged.** If you only import a handful of these dashboards rather than the full set, Home will only list those — it isn't broken, it's accurately showing what exists in your Grafana. If you import a dashboard from this repo and it doesn't appear here, check that it kept its `operational-reports` tag (all 24 of the others carry it already; this only matters if you've edited a dashboard's tags yourself).

## How to import

1. Follow the **[Deploy guide](../Deploying-to-a-New-Grafana-Environment.md)** for the shared mechanics. This page only covers what's specific to Home.
2. Import `spectrum-home.json`. It has nothing to configure on its own — import it any time, before or after the rest.

## Datasource

None — this dashboard has no panels that query data.

## Variables

None.

## Troubleshooting

| Symptom | How obvious | Likely cause | Fix |
|---|---|---|---|
| A dashboard you imported doesn't show up in the list | Quiet | It lost its `operational-reports` tag, or you haven't imported it yet | Check the dashboard's tags in **Dashboard settings → General** |
| List shows fewer than 30 even though you imported more | Not a bug | You've imported fewer than 30 tagged dashboards | Nothing to fix — the list only shows what exists |

## Safe to change by hand

Everything — title, the panel's tag filter, `maxItems`, layout. This page has no drill-down links depending on its uid the way Device Detail does, so it's low-risk to customize.
