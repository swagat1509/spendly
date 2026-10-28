import sqlite3
from datetime import date, timedelta
from pathlib import Path

from werkzeug.security import generate_password_hash

DB_PATH = Path(__file__).resolve().parent.parent / "expense_tracker.db"


def get_db():
    """Return a SQLite connection with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Create all tables if they do not already exist."""
    conn = get_db()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT    NOT NULL,
            email         TEXT    NOT NULL UNIQUE,
            password_hash TEXT    NOT NULL,
            created_at    TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS expenses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL REFERENCES users (id) ON DELETE CASCADE,
            amount      REAL    NOT NULL,
            category    TEXT    NOT NULL,
            date        TEXT    NOT NULL,
            description TEXT    NOT NULL DEFAULT '',
            created_at  TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    conn.commit()
    conn.close()


def seed_db():
    """Insert sample data for development. Safe to run more than once."""
    conn = get_db()
    existing = conn.execute(
        "SELECT id FROM users WHERE email = ?", ("demo@spendly.test",)
    ).fetchone()
    if existing:
        conn.close()
        return

    cursor = conn.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.test", generate_password_hash("demo1234")),
    )
    user_id = cursor.lastrowid

    today = date.today()
    sample_expenses = [
        (45.50, "Food", today - timedelta(days=1), "Lunch with colleagues"),
        (120.00, "Transport", today - timedelta(days=2), "Monthly bus pass"),
        (60.25, "Groceries", today - timedelta(days=4), "Weekly groceries"),
        (15.00, "Entertainment", today - timedelta(days=6), "Movie tickets"),
        (899.99, "Utilities", today - timedelta(days=9), "Electricity bill"),
    ]
    conn.executemany(
        "INSERT INTO expenses (user_id, amount, category, date, description) "
        "VALUES (?, ?, ?, ?, ?)",
        [
            (user_id, amount, category, expense_date.isoformat(), description)
            for amount, category, expense_date, description in sample_expenses
        ],
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    seed_db()
    print(f"Database ready at {DB_PATH}")
