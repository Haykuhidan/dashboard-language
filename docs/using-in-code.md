# Using it in code

Copy-paste starters so every dashboard pulls from the same values. Keep these in one shared module (for example `helios_style.py`) instead of retyping hex codes.

## Python constants

```python
# helios_style.py: Helios Dashboard Language (dark theme)
CAT_YELLOW = "#FFCD11"
CAT_BLUE   = "#2F80ED"
CAT_TEAL   = "#20B2AA"
CAT_GREEN  = "#27AE60"
CAT_ORANGE = "#F2994A"
CAT_RED    = "#D64545"
CAT_PURPLE = "#9B51E0"
CAT_SLATE  = "#65717E"
CAT_GRAY   = CAT_SLATE
CAT_DARK   = "#111820"   # page background
CAT_PANEL  = "#18222D"   # cards / charts
CAT_BORDER = "#334250"   # outlines, rules

CHROME     = "#0B1117"   # header bar
GRIDLINE   = "#243140"
TEXT       = "#E6EBF0"
TEXT_MUTED = "#9AA7B4"

# Meaning, not hue: use these names in chart code
HIGHLIGHT  = CAT_YELLOW
SERIES     = [CAT_BLUE, CAT_TEAL, CAT_PURPLE, CAT_ORANGE]  # max 4, then OTHER
OTHER      = CAT_SLATE
STATUS     = {"good": CAT_GREEN, "warn": CAT_ORANGE, "bad": CAT_RED,
              "info": CAT_BLUE, "neutral": CAT_SLATE}

FONT = '"Segoe UI", system-ui, -apple-system, Roboto, Arial, sans-serif'
```

## Plotly template (Plotly, Dash, Streamlit)

```python
import plotly.graph_objects as go
import plotly.io as pio
from helios_style import *

pio.templates["helios"] = go.layout.Template(layout=dict(
    font=dict(family=FONT, size=12, color=TEXT_MUTED),
    title=dict(font=dict(size=15, color=TEXT), x=0, xanchor="left"),
    paper_bgcolor=CAT_PANEL, plot_bgcolor=CAT_PANEL,
    colorway=SERIES,
    margin=dict(l=48, r=16, t=48, b=40),
    xaxis=dict(showgrid=False, linecolor=CAT_BORDER, ticks="", tickfont=dict(size=11)),
    yaxis=dict(gridcolor=GRIDLINE, zeroline=False, linecolor=CAT_BORDER, tickfont=dict(size=11)),
    legend=dict(orientation="h", y=1.08, x=0, font=dict(size=11)),
    hoverlabel=dict(bgcolor="#1F2B38", bordercolor=CAT_BORDER, font=dict(color=TEXT)),
))
pio.templates.default = "helios"
```

For a highlight chart, colour bars by meaning: `marker_color=[HIGHLIGHT if s == "Ruwais" else CAT_BLUE for s in sites]`.

## matplotlib

```python
import matplotlib as mpl
from helios_style import *
mpl.rcParams.update({
    "figure.facecolor": CAT_PANEL, "axes.facecolor": CAT_PANEL,
    "axes.edgecolor": CAT_BORDER, "axes.labelcolor": TEXT_MUTED,
    "axes.prop_cycle": mpl.cycler(color=SERIES),
    "axes.grid": True, "axes.grid.axis": "y", "grid.color": GRIDLINE,
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": TEXT_MUTED, "ytick.color": TEXT_MUTED,
    "text.color": TEXT, "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "DejaVu Sans"], "font.size": 11,
})
```

## Web (HTML / React)

Link the generated `tokens.css` and `components/bundle.css` from this system, then use the `hd-*` classes shown on each component card. Set `<html data-theme="dark">` (default) or `data-theme="light"`. Always reference `var(--token)`, never raw hex, so the light theme works for free.

## Power BI

Make a theme JSON with `dataColors` set to `SERIES` + `OTHER`, `background` to `CAT_PANEL`, `foreground` to `TEXT`, and `tableAccent` to `CAT_YELLOW`. Then apply the same title rules: the finding as the title, the measure as the subtitle.
