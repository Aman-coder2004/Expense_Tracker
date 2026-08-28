# Expense Tracker — Project Overview

A **Flask web app** for tracking personal expenses, structured as a step-by-step learning project.

## Tech Stack
- **Backend:** Flask 3.1.3 (Python web framework)
- **Testing:** pytest + pytest-flask
- **Frontend:** HTML templates (Jinja2) with static assets
- **Storage:** Local `database/` directory (file-based, likely JSON/SQLite)

## Current State (Scaffold Phase)
The app is a skeleton with **6 routes**, only 3 implemented:

| Route | Status |
|---|---|
| `/`, `/register`, `/login` | ✅ Implemented (render templates) |
| `/logout`, `/profile`, `/expenses/add`, `/expenses/edit`, `/expenses/delete` | ⏳ Placeholders ("coming in Step X") |

## Planned Features (per route comments)
- **Step 3** — Logout
- **Step 4** — User profile
- **Step 7** — Add expense
- **Step 8** — Edit expense
- **Step 9** — Delete expense

## Project Structure
```
expense-tracker/
├── app.py              # Flask routes
├── requirements.txt    # Dependencies
├── database/           # Data storage
├── static/             # CSS/JS/images
├── templates/          # HTML (landing, register, login)
└── venv/               # Virtual environment
```

It's a **teaching-style project** where each feature is built incrementally.
