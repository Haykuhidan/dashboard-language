# Chart card

A panel holding one chart: a title that states the finding, a subtitle that says what is measured, the plot, and a source line.

- **Title = the takeaway** ("Ruwais leads engine hours"), subtitle = the measure and period ("Engine hours by site, last 7 days"). If there's no clear finding yet, the measure becomes the title.
- **Colour order:** `series-1` blue → `series-2` teal → `series-3` purple → `series-4` orange (only when no status colour is on the view). Anything past four goes into `series-other` slate as "Other" — or switch to small multiples or a table.
- **Highlight, don't rainbow:** when the point is one bar or line, paint it `highlight` (yellow) and the rest one series colour or slate. One highlight per chart.
- Gridlines `gridline`, axis baseline `border`, ticks `caption` in `text-muted`. Horizontal gridlines only; no chart borders, 3D, or gradients.
- Bars: horizontal when labels are long, sorted by value, corners `radius-sm`, value labels at the end instead of an x-axis. Bars start at zero.
- Lines: `stroke-line` (2px), the focus line 3px; label the end of a line with its value instead of a legend where possible. Targets are a dashed `series-other` line, named in the legend or footer.
- Plot heights: `chart-sm` 160, `chart-md` 260 (default), `chart-lg` 360 (one hero per page).
- Legend above the plot, in series order, `caption` style.
