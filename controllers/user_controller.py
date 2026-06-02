from database.connection import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import sqlite3

def register_user(data):
    username = data.get("username")
    email    = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return {"message": "All fields are required"}, 400

    hashed_password = generate_password_hash(password)

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        return {"message": "Username or email already exists"}, 400
    finally:
        conn.close()

    return {"message": "User registered successfully"}, 201


def login_user(data):
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"message": "Username and password are required"}, 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user is None or not check_password_hash(user["password"], password):
        return {"message": "Invalid username or password"}, 401

    token = create_access_token(identity=str(user["id"]))
    return {"token": token}, 200
