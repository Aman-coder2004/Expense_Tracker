


from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

from database.db import init_db, seed_db, create_user, get_user_by_email, get_user_by_id
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "dev-secret-key-for-spendly"


# ------------------------------------------------------------------ #
# Database initialization                                              #
# ------------------------------------------------------------------ #
# Run inside an app context so the data layer is ready before the first
# request lands. Both functions are idempotent (CREATE TABLE IF NOT EXISTS
# + seed short-circuit when users already exist).
with app.app_context():
    init_db()
    seed_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("profile"))

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not email or not password:
            return render_template("register.html", error="All fields are required")

        hashed_password = generate_password_hash(password)
        try:
            create_user(name, email, hashed_password)
            flash("Registration successful! Please log in.")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            return render_template("register.html", error="Email already registered")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return render_template("login.html", error="All fields are required")

        user = get_user_by_email(email)
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            flash("Welcome back!")
            return redirect(url_for("profile"))

        return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully")
    return redirect(url_for("landing"))


@app.route("/profile")
def profile():
    user_id = session.get("user_id")
    if not user_id:
    if not user_id:
        flash("Please log in to view your profile")
        return redirect(url_for("login"))
    user = get_user_by_id(user_id)
    if not user:
        flash("User not found")
        return redirect(url_for("logout"))
    # Hardcoded data as per spec for now
    stats = {
        "total_spent": "₹12,450",
        "transaction_count": 42,
        "top_category": "Food"
    }
    recent_transactions = [
        {"date": "2026-09-01", "category": "Food", "description": "Lunch at cafe", "amount": 250},
        {"date": "2026-08-30", "category": "Transport", "description": "Metro card top-up", "amount": 80},
        {"date": "2026-08-28", "category": "Bills", "description": "Electricity bill", "amount": 1200},
    ]
    category_breakdown = [
        {"category": "Food", "percentage": 35, "color": "var(--accent)"},
        {"category": "Transport", "percentage": 20, "color": "var(--accent-2)"},
        {"category": "Bills", "percentage": 45, "color": "var(--ink)"},
    ]
    return render_template("profile.html", user=user, stats=stats, transactions=recent_transactions, categories=category_breakdown)


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
