# Dashboard layout

How a full page is assembled: header, filter bar, page title, a KPI row, then panels on a 12-column grid.

1. **Header** (always) → **filter bar** (if anything is filterable) → **page title + one-line scope**.
2. **KPI row**: 3–5 tiles, `hd-span-3` or `hd-span-4` each. One may be the focus tile.
3. **Hero chart** (`hd-span-7`/`8`, `chart-lg` or `chart-md`) beside its supporting **table** (`hd-span-5`/`4`).
4. Further rows of 6+6 or 4+4+4. Read order is top-left to bottom-right, most important first.

- Gutter and panel padding are both `space-4` (16px); page margins `space-4`, `space-6` on wide screens.
- Every panel touches the grid; no floating or overlapping cards.
- If a page needs more than ~8 panels, split it into tabs or pages.
