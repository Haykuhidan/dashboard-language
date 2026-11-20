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
