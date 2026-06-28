import sqlite3
from pathlib import Path

# Create data directory if it doesn't exist
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "users.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            username TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_user(user_id: int, first_name: str, username: str | None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, first_name, username)
        VALUES (?, ?, ?)
    """, (user_id, first_name, username))

    conn.commit()
    conn.close()


def get_total_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    total = cursor.fetchone()[0]

    conn.close()
    return total


def get_all_user_ids():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT user_id FROM users")
    users = [row[0] for row in cursor.fetchall()]

    conn.close()
    return users