# Helios Dashboard Language

Shared colours, type and layout rules for every Helios Cognition dashboard.

## What's here

| Folder | Use it for |
| --- | --- |
| `powerbi/` | Power BI themes. **Helios-Dark.json** is the default; **Helios-Light.json** is for reports and print. |
| `python/helios_style.py` | Colour constants for Plotly, Dash, Streamlit and matplotlib. |
| `web/` | `tokens.json` (every colour, size and spacing value) and `helios-components.css` (header, KPI tiles, tables, badges). |
| `docs/` | The rules: colour meaning, writing chart titles, and how each component works. |

## Power BI in 3 steps

1. Download `powerbi/Helios-Dark.json`.
2. In Power BI Desktop, go to **View → Themes → Browse for themes** and pick the file.
3. Lay the page out at 1280 × 720:
   - header bar at x 16, y 16, 1248 × 48, fill `#0B1117`;
   - 4 KPI cards at y 128, each 300 × 120;
   - main chart at x 16, y 264, 724 × 440;
   - table at x 756, y 264, 508 × 440.

## The five rules

1. **Yellow `#FFCD11` is a spotlight.** Use it for one thing per view: the bar, line or KPI that matters.
2. **Blue, teal and purple are categories. Green, orange and red mean good, warning and bad.** Never swap them.
3. **Chart titles state what the chart shows:** "Downtime spiked at Ruwais on Tuesday", not "Downtime chart".
4. **Always show the comparison period and data freshness:** "vs last week", "Data to 20 Nov, 06:00 GST".
5. **Panels on a 16 px grid**, with 1px borders and no shadows.

## Palette

| Name | Hex | Meaning |
| --- | --- | --- |
| CAT_YELLOW | `#FFCD11` | Highlight / brand |
| CAT_BLUE | `#2F80ED` | Series 1, info |
| CAT_TEAL | `#20B2AA` | Series 2 |
| CAT_PURPLE | `#9B51E0` | Series 3 |
| CAT_GREEN | `#27AE60` | Good |
| CAT_ORANGE | `#F2994A` | Warning |
| CAT_RED | `#D64545` | Bad |
| CAT_SLATE | `#65717E` | Other / comparison |
| CAT_DARK | `#111820` | Page background |
| CAT_PANEL | `#18222D` | Cards |
| CAT_BORDER | `#334250` | Borders |

The official CAT logo isn't included. Get it from the brand portal.
