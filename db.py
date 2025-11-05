import sqlite3
from datetime import datetime

DB_NAME = "fridge.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS food_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        quantity TEXT,
        location TEXT,
        expiry_date TEXT NOT NULL,
        added_at TEXT
    );
    """)
    conn.commit()
    conn.close()


def add_item(name, category, quantity, location, expiry_date):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    INSERT INTO food_items (name, category, quantity, location, expiry_date, added_at)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, category, quantity, location, expiry_date, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def get_all_items():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, name, category, quantity, location, expiry_date, added_at FROM food_items ORDER BY expiry_date ASC")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_item(item_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM food_items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    add_item("Milk", "Dairy", "1L", "Fridge", "2025-11-10")
    print(get_all_items())