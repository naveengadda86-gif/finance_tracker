from database.connection import get_db
import sqlite3

def add_category(data):
    name = data.get("name")

    if not name:
        return {"message": "Category name is required"}, 400

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        return {"message": "Category already exists"}, 400
    finally:
        conn.close()

    return {"message": "Category added successfully"}, 201


def get_all_categories():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    conn.close()

    result = []
    for cat in categories:
        result.append({"id": cat["id"], "name": cat["name"]})

    return result, 200
