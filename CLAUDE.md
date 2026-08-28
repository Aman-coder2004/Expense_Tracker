# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Spendly** — a Flask web app for tracking personal expenses (Indian rupee-focused, per the UI). It is structured as a **step-by-step learning project** where features are added incrementally. Currently in the **scaffold phase**.

- **Backend:** Flask 3.1.3, Werkzeug 3.1.6
- **Testing:** pytest 8.3.5, pytest-flask 1.3.0
- **Frontend:** Jinja2 templates, vanilla CSS (`static/css/style.css`), vanilla JS (`static/js/main.js`)
- **Storage:** SQLite (file-based at the repo root as `expense_tracker.db`, currently empty)
- **Python:** 3.x, run inside `venv/`

## Common Commands

Set up the virtual environment (one-time):
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

Run the dev server (debug mode, port **5001** — not the Flask default):
```bash
python app.py
```

Run the full test suite:
```bash
pytest
```

Run a single test file:
```bash
pytest tests/test_app.py
```

Run a single test by name:
```bash
pytest tests/test_app.py::test_login
```

## Architecture

### Entry point — `app.py`
A single-file Flask app. Routes are split into two groups by a section comment:
- **Implemented routes** (render templates): `/`, `/register`, `/login`, `/terms`, `/privacy`
- **Placeholder routes** (return placeholder strings, marked "coming in Step X"): `/logout`, `/profile`, `/expenses/add`, `/expenses/<int:id>/edit`, `/expenses/<int:id>/delete`

Step numbers in the placeholders are part of the curriculum ordering:
- **Step 3** — Logout
- **Step 4** — User profile
- **Step 7** — Add expense
- **Step 8** — Edit expense
- **Step 9** — Delete expense

### Database layer — `database/`
- `database/__init__.py` — empty package marker
- `database/db.py` — **stub**, students implement in Step 1. Expected API (per the file's docstring):
  - `get_db()` — returns a SQLite connection with `row_factory` set to `sqlite3.Row` and foreign keys enabled
  - `init_db()` — creates all tables using `CREATE TABLE IF NOT EXISTS`
  - `seed_db()` — inserts sample data for development

When implementing these, follow the documented signature — the test suite (once added) will import from this module by name.

### Templates — `templates/`
- `base.html` — shared layout: navbar (brand "Spendly", Sign in / Get started links), footer (Terms/Privacy), loads Google Fonts (DM Serif Display + DM Sans) and `style.css`/`main.js`. Blocks: `title`, `head`, `content`, `scripts`.
- `landing.html` — marketing landing page with hero, feature cards, CTA, and a lazy-loaded YouTube modal ("How it works")
- `register.html`, `login.html` — auth forms (POST to `/register` and `/login` respectively; expect an `error` variable for inline error display)
- `terms.html`, `privacy.html` — static legal pages

### Static assets — `static/`
- `css/style.css` — design tokens at the top (CSS custom properties for color palette, fonts, radii, `--max-width: 1200px`, `--auth-width: 440px`). Color scheme is editorial/magazine-style: paper background, deep green accent (`--accent: #1a472a`), warm orange secondary accent. Indian rupee (`₹`) is the currency symbol.
- `js/main.js` — currently a one-line stub

### Design system notes
- **Currency:** ₹ (Indian rupee) — all amounts and the brand voice use this
- **Brand name:** "Spendly" (not "Expense Tracker" — the repo folder name is generic)
- **Voice:** warm, editorial — "Track every rupee. Own your finances." Avoid generic SaaS tone
- **Fonts:** DM Serif Display for display text, DM Sans for body

## Project structure
```
expense-tracker/
├── app.py              # All Flask routes (single file)
├── requirements.txt    # Pinned deps
├── database/
│   ├── __init__.py     # (empty)
│   └── db.py           # Stub — implement in Step 1
├── templates/          # Jinja2 templates (see above)
├── static/
│   ├── css/style.css   # Design system + all styles
│   └── js/main.js      # (stub)
├── venv/               # Local virtual environment (gitignored)
└── expense_tracker.db  # SQLite DB (gitignored, created at runtime)
```

## Things to know before editing

- The dev server runs on **port 5001**, not 5000. If you change it, update any test fixtures and the CLAUDE.md command.
- The `register` and `login` templates POST to `/register` and `/login` but `app.py` only defines GET handlers — implementing POST + form handling is part of the upcoming steps.
- The `.gitignore` covers `venv/`, `expense_tracker.db`, `__pycache__/`, `.env`, and `.claude/plans/` but **not** `venv`. Wait — it does include `venv/`. Confirmed safe to ignore.
- `.claude/settings.local.json` only permits the `Websearch` tool. If the user asks for file edits, plan-mode operations, etc., the harness will prompt.
- There is no `tests/` directory yet. When adding tests, use `pytest` + `pytest-flask` and create a `conftest.py` that exposes the Flask app fixture (the `pytest-flask` `client` fixture is the standard pattern).
- The `app.py` file starts with two blank numbered lines (1, 2) — leave those alone, they are intentional.
- The `Screenshot 2026-03-25 at 12.36.20 AM.png` file in the root is a reference image of the design, not source.
