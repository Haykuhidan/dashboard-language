# Helios Dashboard Language

The shared visual language for every Helios Cognition dashboard: one dark brand frame, quiet panels, Caterpillar yellow for the one thing that matters, and colour that always means something.

Built from the CAT Digital palette (`CAT_YELLOW` … `CAT_BORDER`) and the Helios Cognition header bar. It isn't an official CAT brand standard: when the Helios Tools pages on CAT Digital Confluence say otherwise, they win.

## Principles

1. **Yellow is a spotlight, not paint.** `cat-yellow` marks the single focus on a view: the highlighted series, the focus KPI, the selected filter. If everything is yellow, nothing is.
2. **Colour has a job.** Blue/teal/purple are *categories*. Green/orange/red are *status* (good, warning, bad) and nothing else. Slate is *other, comparison or inactive*.
3. **Panels, not decoration.** Everything sits on a `panel` with a 1px `border`. Borders do the work shadows would; no gradients, glows or 3D.
4. **Numbers first.** Big tabular figures, units muted, a written comparison period, a source line on every chart.
5. **Same frame everywhere.** Same header, filter bar, grid and spacing on every dashboard, so the team's work reads as one product.

## Writing on dashboards

- **Titles state the finding:** "Downtime spiked at Ruwais on Tuesday", not "Downtime chart". The subtitle says what's measured: "Unplanned downtime hours per day".
- Sentence case everywhere: titles, labels, buttons. No ALL CAPS labels.
- Units go in headers and subtitles ("Downtime (h)"), not repeated in every cell.
- Always say the period ("vs last week") and the freshness ("Data to 20 Nov 2026, 06:00 GST").
- Round to what someone acts on: 94.2%, 12.3k, 1,284. Thousands separators always.
- No exclamation marks, no emoji in UI.

## Colour

Two themes share every token name. **Dark is primary** (screens, wall displays, the Helios look); **light** is for reports, print and bright rooms.

| Role | Tokens | Rule |
| --- | --- | --- |
| Frame | `chrome`, `on-chrome`, `on-chrome-muted` | Header bar only. Dark in both themes. |
| Surfaces | `bg` (CAT_DARK) → `panel` (CAT_PANEL) → `panel-raised` | Page → card → hover/selected. |
| Lines | `border` (CAT_BORDER), `gridline` | Panel outlines and rules; chart grids quieter still. |
| Text | `text`, `text-muted`, `link` | All pass 4.5:1 on `bg` and `panel` in both themes. |
| Brand | `cat-yellow`, `highlight`, `highlight-soft`, `on-brand` | The one focus. Text on yellow is always `on-brand` (near-black). |
| Categories | `series-1` blue, `series-2` teal, `series-3` purple, `series-4` orange, `series-other` slate | In this order. Max four, then "Other". |
| Status | `status-good` / `-warn` / `-bad` / `-info` / `-neutral` and their `-soft` tints | Only for state. Always paired with a word or ▲▼. |

The `cat-*` tokens hold Toby's palette exactly in the dark theme. In the light theme, teal, green, orange, red, purple and slate are deepened so marks keep 3:1 on white. Yellow can't reach that on white, so on light it's only ever a fill with dark text on it, or an outline. `CAT_GRAY` is an alias of `CAT_SLATE`, so there's one `cat-slate` token.

## Type

One family: the system UI sans (Segoe UI on the team's Windows machines), so there's nothing to install and dashboards match Teams and Office. Mono (Cascadia Mono / Consolas) is for serials and IDs only.

- Numbers: `kpi-xl` 32px, `kpi-md` 24px, `num` 13px, always with tabular figures (`.hd-num`).
- Text: `page-title` 20px, `panel-title` 15px, `body` 14px, `label` 12px, `caption` 11px (the floor: axis ticks, legends, source lines).

## Space and shape

A 4px base. `space-4` (16px) is the number to remember: panel padding *and* the gap between panels. `radius-md` 8px for panels and the header, `radius-sm` 4px for badges, inputs and bar ends. The only shadow, `shadow-float`, is for tooltips and dropdowns.

## Iconography

Keep icons minimal: ▲ ▼ for deltas, a status dot, ✕ to remove a filter, ▾ for dropdowns. If you need more, use one outline set at 16px, 1.5px stroke, in `text-muted`. Never put icons in KPI tiles or chart titles for decoration.

## Logo

This system ships no logo file. Put the official CAT logo from the brand portal in the header's logo slot, unaltered, at 24px tall. Don't redraw, recolour or stretch it.

## Components

- **App header**: the brand bar.
- **Filter bar**: period, dimensions, freshness.
- **KPI tile**: label, value, delta.
- **Chart card**: titled chart with colour and axis rules.
- **Data table**: compact, right-aligned numbers.
- **Status badge**: dot, tint and word.
- **Dashboard layout**: the 12-column page.

Each one is plain HTML and CSS classes (`hd-*` in `components/bundle.css`), so they work in any stack. For Python dashboards (Plotly, Dash, Streamlit, matplotlib), copy the snippets in **Using it in code**.

## Accessibility checklist

- Text meets 4.5:1 and marks meet 3:1 in the theme you ship. The tokens already do this, so don't swap in raw hex.
- Never rely on colour alone: words on badges, ▲▼ on deltas, direct labels on lines.
- Charts get an `aria-label` or a table alternative. Keyboard focus shows `focus-ring`.
