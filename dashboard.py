from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_PATH = "database/attacks.db"

@app.route("/")
def dashboard():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM attacks
    ORDER BY id DESC
    """)

    attacks = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM attacks")
    total_attacks = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        attacks=attacks,
        total_attacks=total_attacks
    )

if __name__ == "__main__":
    app.run(debug=True)