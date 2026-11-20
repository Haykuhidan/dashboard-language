# App header

The single dark bar across the top of every dashboard: logo, product name, and optionally the page name and a freshness stamp — nothing else.

- **Minimal form** (top): logo + "Helios Cognition". This is the one from the team chat and is the default.
- **Full form**: add a 1px `border` separator, the dashboard name in `on-chrome-muted`, and on the right the last-refresh time.
- Background is `chrome` in **both** themes, so the brand frame is identical whether the page is light or dark. Height `header-height` (48px), corners `radius-md`, side padding `space-4`.
- Product name: 18/24, weight 500, `on-chrome`. Never put it in yellow.
- **Logo:** the slot is 24px tall. Drop in the official logo file from the brand portal (`<img>` inside `.hd-header__logo`). Don't redraw or recolour it; this system ships no logo file.
- No filters, menus or buttons in the header — those belong in the filter bar under it.

```html
<header class="hd-header">
  <span class="hd-header__logo"><img src="cat-logo.svg" alt="Caterpillar"></span>
  <span class="hd-header__product">Helios Cognition</span>
  <span class="hd-header__sep"></span>
  <span class="hd-header__page">Fleet utilisation</span>
  <span class="hd-header__end">Updated 06:00 GST</span>
</header>
```
