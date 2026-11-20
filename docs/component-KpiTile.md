# KPI tile

One number, its label, and how it moved — the first row of almost every dashboard.

- Order is always **label → value → delta + comparison**. The comparison period is written out ("vs last week"), never implied.
- Value: `kpi-xl` (32/36, 600) with tabular figures; the unit is smaller and `text-muted`, attached to the number.
- Delta colour means **good or bad, not up or down**: downtime going up is `status-bad`. Flat is `text-muted`. Always pair colour with ▲ ▼ — so it reads in greyscale.
- Optional sparkline: `series-other` line, last point as a `highlight` dot. No axes.
- `hd-kpi--focus` gives one tile a `cat-yellow` border — the number this dashboard exists for. At most one per page.
- 3–5 tiles per row; tiles wrap below `kpi-min-width`. Round to what matters (94.2%, not 94.2173%).
