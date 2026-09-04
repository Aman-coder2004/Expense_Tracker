# Database access layer for Spendly.
# Implements the data layer foundation described in
# .claude/specs/01_Databse_setup.md (Step 1 — Database Setup).

import sqlite3
from datetime import date, timedelta

from werkzeug.security import generate_password_hash


# SQLite database file lives at the project root.
# `.gitignore` covers *.db so this file is never committed.
DB_PATH = "spendly.db"


def get_db() -> sqlite3.Connection:
    """Open a SQLite connection with row factory + foreign keys enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    # Foreign keys are per-connection in SQLite — must be set every time.
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    """Create the users and expenses tables if they don't already exist."""
    conn = get_db()
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                name          TEXT    NOT NULL,
                email         TEXT    NOT NULL UNIQUE,
                password_hash TEXT    NOT NULL,
                created_at    TEXT    DEFAULT (datetime('now'))
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                amount      REAL    NOT NULL,
                category    TEXT    NOT NULL,
                date        TEXT    NOT NULL,
                description TEXT,
                created_at  TEXT    DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def create_user(name: str, email: str, password_hash: str) -> None:
    """Insert a new user into the database.

    Raises sqlite3.IntegrityError if the email is already registered.
    """
    conn = get_db()
    try:
        conn.execute(
            """
            INSERT INTO users (name, email, password_hash)
            VALUES (?, ?, ?)
            """,
            (name, email, password_hash),
        )
        conn.commit()
    finally:
        conn.close()


def get_user_by_email(email: str):
    """Retrieve a user record by email."""
    conn = get_db()
    try:
        return conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()
    finally:
        conn.close()


def get_user_by_id(user_id: int):
    """Retrieve a user record by ID."""
    conn = get_db()
    try:
        return conn.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()
    finally:
        conn.close()


def seed_db() -> None:
    """Insert demo user + sample expenses exactly once.

    Short-circuits if `users` already contains data, so repeated app
    startups don't duplicate seed rows.
    """
    conn = get_db()
    try:
        existing = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        if existing:
            return

        # --- demo user ---------------------------------------------------- #
        cursor = conn.execute(
            """
            INSERT INTO users (name, email, password_hash)
            VALUES (?, ?, ?)
            """,
            ("Demo User", "demo@spendly.com", generate_password_hash("demo123")),
        )
        user_id = cursor.lastrowid

        # --- 8 sample expenses spread across the current month ------------ #
        # All values use parameterized placeholders — never f-strings in SQL.
        today = date.today()
        sample_expenses = [
            (user_id, 250.0,  "Food",          today,                         "Lunch at cafe"),
            (user_id, 80.0,   "Transport",     today - timedelta(days=2),     "Metro card top-up"),
            (user_id, 1200.0, "Bills",         today - timedelta(days=5),     "Electricity bill"),
            (user_id, 450.0,  "Health",        today - timedelta(days=7),     "Pharmacy"),
            (user_id, 599.0,  "Entertainment", today - timedelta(days=10),    "Movie ticket"),
            (user_id, 1499.0, "Shopping",      today - timedelta(days=14),    "New headphones"),
            (user_id, 300.0,  "Other",         today - timedelta(days=18),    "Stationery"),
            (user_id, 175.0,  "Food",          today - timedelta(days=22),    "Groceries"),
        ]

        conn.executemany(
            """
            INSERT INTO expenses (user_id, amount, category, date, description)
            VALUES (?, ?, ?, ?, ?)
            """,
            sample_expenses,
        )
        conn.commit()
    finally:
        conn.close()
