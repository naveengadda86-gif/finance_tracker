import sqlite3

def get_db():
    conn = sqlite3.connect("finance.db")
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn

def create_tables():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    NOT NULL UNIQUE,
            email    TEXT    NOT NULL UNIQUE,
            password TEXT    NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT    NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            amount      REAL    NOT NULL,
            description TEXT,
            date        TEXT    NOT NULL
        )
    """)

    conn.commit()
    conn.close()
