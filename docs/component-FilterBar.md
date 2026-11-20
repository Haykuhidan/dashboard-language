# Filter bar

The row of controls under the header that scopes everything on the page — time period first, then dimensions, then the data-freshness note on the right.

- **Period** is always a segmented control (24h · 7d · 30d · QTD …). The selected segment is `panel-raised` with a 2px `cat-yellow` underline — the yellow is the "you are here" cue.
- **Dimensions** (region, site, model) are dropdowns with a 1px `text-muted` border (3:1, a visible control edge). An applied filter becomes a chip with a `cat-yellow` border on `highlight-soft`, removable with ✕.
- Right-aligned: "Data to <date>, <time> <zone>" in `caption`. Every dashboard says how fresh it is.
- Filters apply to the whole page. A filter that affects only one panel lives in that panel's header.
