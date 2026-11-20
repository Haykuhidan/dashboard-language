# Data table

A compact table on a panel for ranked lists and drill-down detail — the place for exact values.

- Rows `row-height` (36px); row rules `gridline`, header rule `border`. No zebra stripes, no vertical lines.
- Headers in `label` style, `text-muted`, sentence case, with units in the header ("Downtime (h)"), not in every cell.
- **Numbers right-aligned with tabular figures** (`.r`); text left-aligned. IDs and serials in `code` mono, `text-muted`.
- An inline bar (`hd-bar` in a `hd-bar-track`) may sit beside the one key number to show proportion.
- Highlight at most one row (`is-focus`, `highlight-soft` background, its bar in `highlight`).
- Sort by the column that answers the panel title; show the sort. Over ~15 rows, paginate or put the table on its own page.
