from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# -----------------------------
# Create Database
# -----------------------------
def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

init_db()

# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Login
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid Username or Password")

    return render_template("login.html")


# -----------------------------
# Dashboard
# -----------------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# -----------------------------
# Add Course
# -----------------------------
@app.route("/add-course", methods=["GET", "POST"])
def add_course():

    if request.method == "POST":

        course = request.form.get("course")

        if course:

            conn = sqlite3.connect("database.db")
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO courses (name) VALUES (?)",
                (course,)
            )

            conn.commit()
            conn.close()

            return redirect(url_for("courses"))

    return render_template("add_course.html")


# -----------------------------
# View Courses
# -----------------------------
@app.route("/courses")
def courses():

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM courses")

    data = cur.fetchall()

    conn.close()

    return render_template(
        "courses.html",
        courses=data
    )


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )