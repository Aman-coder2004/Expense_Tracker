---
name: spendly-ui-designer
description: Designs and generates modern, production-ready UI for Spendly, a personal expense tracker built on Flask + Jinja2 + vanilla CSS (github.com/Aman-coder2004/Expense_Tracker). Produces clean fintech-style pages and components — cards, forms, tables, dashboards, modals, nav bars — with consistent spacing, soft shadows, rounded corners, and Lucide icons. Use whenever the user asks to design, build, create, redesign, improve, or style any Spendly page, screen, section, or component — e.g. "design the X page", "create UI for X", "build a component for X", "make the X look better", "redesign X", "add a dashboard/modal/table for X", or any request about Spendly's frontend, layout, CSS, or visual polish. Trigger even when Spendly isn't named explicitly if context is clearly about it (Flask + Jinja2 expense-tracker templates, expense/budget/category pages). Consult before writing any Spendly HTML/CSS so output matches the design system, not generic Bootstrap defaults.
---

# Spendly UI Designer

Generates and edits Flask + Jinja2 + vanilla CSS UI for Spendly, a personal expense tracker. Every output should look like a real fintech product — not a tutorial CRUD app.

## Repo conventions (Aman-coder2004/Expense_Tracker)

Match this existing structure. Don't invent a different layout unless the user's actual files show otherwise — if unsure, ask to see the current `templates/` or `static/` contents rather than guessing.

```
app.py                     # Flask app
templates/
  base.html                 # shared layout: <head>, nav, {% block content %}
  <page>.html                # extends base.html, fills content block
static/
  css/
    tokens.css               # design tokens (create if missing)
    style.css                # global/base styles
    components.css            # reusable component classes (cards, buttons, modals...)
  js/
    (page-specific JS, e.g. modal toggles, chart init)
database/
```

- Templates extend `base.html` via `{% extends "base.html" %}` and `{% block content %}...{% endblock %}`.
- Link CSS in `base.html` `<head>`: `tokens.css` → `style.css` → `components.css`, in that order, plus any page-specific file.
- Use Jinja2 idiomatically: `{% for %}`, `{% if %}`, `url_for('endpoint')` for links/forms, never hardcoded paths.
- No JS frameworks — vanilla JS only, in `static/js/`, linked at the bottom of the relevant template.

## Design tokens (default palette)

Use these as CSS custom properties in `static/css/tokens.css` unless the user already has tokens defined — then read and reuse theirs instead.

```css
:root {
  /* Brand */
  --color-primary: #4F46E5;       /* indigo — primary actions, active states */
  --color-primary-hover: #4338CA;
  --color-primary-soft: #EEF2FF;  /* tinted backgrounds behind primary */

  /* Semantic (income/expense/status) */
  --color-income: #16A34A;
  --color-income-soft: #F0FDF4;
  --color-expense: #DC2626;
  --color-expense-soft: #FEF2F2;
  --color-warning: #D97706;
  --color-warning-soft: #FFFBEB;

  /* Neutrals */
  --color-bg: #F9FAFB;
  --color-surface: #FFFFFF;
  --color-border: #E5E7EB;
  --color-text: #111827;
  --color-text-muted: #6B7280;
  --color-text-subtle: #9CA3AF;

  /* Spacing scale (4px base) */
  --space-1: 4px;  --space-2: 8px;  --space-3: 12px;
  --space-4: 16px; --space-5: 24px; --space-6: 32px; --space-8: 48px;

  /* Radius */
  --radius-sm: 8px; --radius-md: 12px; --radius-lg: 16px; --radius-full: 999px;

  /* Shadows — soft, never harsh */
  --shadow-sm: 0 1px 2px rgba(16, 24, 40, 0.05);
  --shadow-md: 0 4px 12px rgba(16, 24, 40, 0.08);
  --shadow-lg: 0 8px 24px rgba(16, 24, 40, 0.10);

  /* Typography */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --text-xs: 12px; --text-sm: 14px; --text-base: 16px;
  --text-lg: 18px; --text-xl: 24px; --text-2xl: 32px;
}
```

Load Inter via Google Fonts `<link>` in `base.html` (or note it as a dependency if the user prefers self-hosted fonts).

## Lucide icons

Use the CDN script, added once in `base.html` before `</body>`:

```html
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
<script>lucide.createIcons();</script>
```

Reference icons as `<i data-lucide="wallet"></i>` inline. Pick icons that match meaning (e.g. `trending-up`/`trending-down` for income/expense, `pie-chart` for breakdowns, `plus-circle` for add actions, `trash-2` for delete, `x` for modal close). Re-run `lucide.createIcons()` after any JS that injects new icon markup dynamically (e.g. rows added without a page reload).

## Component patterns

Build these as reusable classes in `components.css`, not one-off inline styles. Always use the tokens above (`var(--color-primary)` etc.) rather than hardcoded hex values, so a future palette change is a one-file edit.

### Cards
`.card` — `background: var(--color-surface)`, `border-radius: var(--radius-lg)`, `box-shadow: var(--shadow-sm)`, `padding: var(--space-5)`, `border: 1px solid var(--color-border)`. Stat cards (e.g. "Total Spent") pair a `--text-2xl` bold number with a `--text-sm` muted label and a small colored icon badge in the corner.

### Forms
Inputs: `border: 1px solid var(--color-border)`, `border-radius: var(--radius-sm)`, `padding: var(--space-3) var(--space-4)`, clear `:focus` state with `border-color: var(--color-primary)` + subtle ring shadow. Labels above inputs, `--text-sm`, `--color-text-muted`. Primary submit buttons use `--color-primary` background, white text, `--radius-md`, hover darkens to `--color-primary-hover`. Secondary/cancel buttons are outline or ghost style.

### Tables
Use for transaction lists. Header row: `--text-xs`, uppercase, `--color-text-subtle`, bottom border. Rows: generous vertical padding (`--space-4`), subtle hover background, no heavy grid lines — rely on whitespace and a single bottom border per row. Amount columns right-aligned; income in `--color-income`, expenses in `--color-expense`, often prefixed with `+`/`-`. Category shown as a small pill badge (`--radius-full`, soft background tint matching category color).

### Dashboards
Grid layout: top row of 3–4 stat cards (`display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: var(--space-5)`), followed by a two-column section (chart/breakdown + recent transactions list) that stacks to one column below ~900px. Charts: if the user hasn't specified a library, ask, or suggest a minimal option (Chart.js via CDN, matching token colors) rather than assuming.

### Modals
Overlay: fixed, full-viewport, `rgba(17,24,39,0.5)` backdrop. Modal box: `.card` styling, `max-width: 480px`, centered, `--shadow-lg`. Header row with title + `<i data-lucide="x">` close button. Toggle via a small vanilla JS snippet (`.hidden { display: none }` class toggle), not inline `style=`.

## Layout & responsiveness

- Mobile-first or at minimum fully responsive: stat grids and two-column dashboards collapse to single column under ~768px.
- Consistent page shell: sidebar or top nav (pick one and stay consistent) + main content area with `padding: var(--space-6)` and `max-width: 1200px; margin: 0 auto`.
- Use `gap` for spacing between flex/grid children instead of margin hacks.

## Workflow for each request

1. **Identify scope**: one component, one page, or a multi-page redesign? Confirm scope for anything ambiguous (e.g. "make it look better" with no target).
2. **Check for existing tokens/CSS**: if the user has shared or uploaded their current `templates/`/`static/` files, reuse their existing tokens, class names, and structure instead of the defaults above. Defaults are a fallback for a fresh build, not a mandate to overwrite an established style.
3. **Generate**: full Jinja2 template (extending `base.html`) + any new/updated CSS in the appropriate file (`components.css` for reusable pieces, page-specific CSS only if truly one-off). Include realistic placeholder data (sample transactions, categories, amounts) so the page is easy to preview, using Jinja2 loop syntax over a sample list rather than hardcoding rows.
4. **Explain briefly**: 2-3 lines on what was built and where the files go — don't over-explain design choices unless asked.

## What to avoid

- Generic Bootstrap-card-with-shadow look, default browser form styling, harsh pure-black text/borders, saturated primary colors without a soft/tinted counterpart, icon fonts other than Lucide, inline `style=` attributes for anything reusable, hardcoded colors instead of CSS variables.