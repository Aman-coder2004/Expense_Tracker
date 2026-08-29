import random
import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash
from database.db import get_db

def generate_indian_user():
    first_names = ["Rahul", "Anjali", "Amit", "Priya", "Sandeep", "Sneha", "Vikram", "Kavita", "Arjun", "Deepika"]
    last_names = ["Sharma", "Verma", "Gupta", "Malhotra", "Iyer", "Reddy", "Singh", "Patel", "Chatterjee", "Nair"]

    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"

    # Derived email: first.last{num}@gmail.com
    email = f"{first.lower()}.{last.lower()}{random.randint(10, 999)}@gmail.com"
    password_hash = generate_password_hash("password123")
    created_at = datetime.now().isoformat()

    return name, email, password_hash, created_at

def seed_user():
    conn = get_db()
    try:
        while True:
            name, email, password_hash, created_at = generate_indian_user()

            # Check if email exists
            existing = conn.execute("SELECT 1 FROM users WHERE email = ?", (email,)).fetchone()
            if not existing:
                break

        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
            (name, email, password_hash, created_at)
        )
        conn.commit()

        user_id = cursor.lastrowid
        print(f"User created successfully:")
        print(f"ID: {user_id}")
        print(f"Name: {name}")
        print(f"Email: {email}")

    finally:
        conn.close()

if __name__ == "__main__":
    seed_user()
