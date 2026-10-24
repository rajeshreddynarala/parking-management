from datetime import datetime
from pathlib import Path
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-secret-key"
DB_PATH = Path(__file__).with_name("parking.db")
FLOORS = 5
SLOTS_PER_FLOOR = 10
HOURLY_RATE = 20  # INR per started hour

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with db() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS slots (
            id INTEGER PRIMARY KEY AUTOINCREMENT, floor INTEGER NOT NULL,
            slot_number INTEGER NOT NULL, status TEXT NOT NULL DEFAULT 'Available',
            UNIQUE(floor, slot_number))""")
        conn.execute("""CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_number TEXT NOT NULL,
            vehicle_type TEXT NOT NULL, floor INTEGER NOT NULL, slot_number INTEGER NOT NULL,
            entry_time TEXT NOT NULL, exit_time TEXT, fee REAL,
            status TEXT NOT NULL DEFAULT 'Parked')""")
        for floor in range(1, FLOORS + 1):
            for slot in range(1, SLOTS_PER_FLOOR + 1):
                conn.execute("INSERT OR IGNORE INTO slots (floor, slot_number) VALUES (?, ?)", (floor, slot))

# Create the database when the app starts locally or on a hosting service.
init_db()

@app.route("/")
def index():
    with db() as conn:
        floors = []
        for floor in range(1, FLOORS + 1):
            slots = conn.execute("SELECT * FROM slots WHERE floor=? ORDER BY slot_number", (floor,)).fetchall()
            occupied = sum(s["status"] == "Occupied" for s in slots)
            floors.append({"number": floor, "total": len(slots), "occupied": occupied,
                           "available": len(slots)-occupied, "slots": slots})
        active = conn.execute("SELECT * FROM sessions WHERE status='Parked' ORDER BY entry_time DESC").fetchall()
    totals = {"total": FLOORS*SLOTS_PER_FLOOR,
              "occupied": sum(f["occupied"] for f in floors),
              "available": sum(f["available"] for f in floors), "active": len(active)}
    return render_template("index.html", floors=floors, active=active, totals=totals)

@app.route("/entry", methods=["GET", "POST"])
def entry():
    if request.method == "POST":
        number = request.form.get("vehicle_number", "").strip().upper()
        kind = request.form.get("vehicle_type", "Car")
        if not number:
            flash("Enter a vehicle registration number.", "error")
            return redirect(url_for("entry"))
        with db() as conn:
            existing = conn.execute("SELECT id FROM sessions WHERE vehicle_number=? AND status='Parked'", (number,)).fetchone()
            if existing:
                flash("This vehicle already has an active parking session.", "error")
                return redirect(url_for("entry"))
            slot = conn.execute("SELECT * FROM slots WHERE status='Available' ORDER BY floor, slot_number LIMIT 1").fetchone()
            if slot is None:
                flash("Parking is full on all five floors.", "error")
                return redirect(url_for("entry"))
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn.execute("""INSERT INTO sessions
                (vehicle_number, vehicle_type, floor, slot_number, entry_time, status)
                VALUES (?, ?, ?, ?, ?, 'Parked')""",
                (number, kind, slot["floor"], slot["slot_number"], now))
            conn.execute("UPDATE slots SET status='Occupied' WHERE id=?", (slot["id"],))
        flash(f"Vehicle parked on Floor {slot['floor']}, Slot {slot['slot_number']}.", "success")
        return redirect(url_for("index"))
    return render_template("entry.html")

@app.route("/exit/<int:session_id>", methods=["POST"])
def vehicle_exit(session_id):
    with db() as conn:
        session = conn.execute("SELECT * FROM sessions WHERE id=? AND status='Parked'", (session_id,)).fetchone()
        if session is None:
            flash("Active parking record not found.", "error")
            return redirect(url_for("index"))
        now = datetime.now()
        entered = datetime.strptime(session["entry_time"], "%Y-%m-%d %H:%M:%S")
        seconds = max(0, (now-entered).total_seconds())
        hours = max(1, int(seconds // 3600) + (1 if seconds % 3600 else 0))
        fee = hours * HOURLY_RATE
        conn.execute("UPDATE sessions SET exit_time=?, fee=?, status='Completed' WHERE id=?",
                     (now.strftime("%Y-%m-%d %H:%M:%S"), fee, session_id))
        conn.execute("UPDATE slots SET status='Available' WHERE floor=? AND slot_number=?",
                     (session["floor"], session["slot_number"]))
    flash(f"Exit recorded. Parking fee: ₹{fee:.2f} ({hours} hour(s)).", "success")
    return redirect(url_for("records"))

@app.route("/records")
def records():
    with db() as conn:
        rows = conn.execute("SELECT * FROM sessions ORDER BY id DESC LIMIT 200").fetchall()
    return render_template("records.html", records=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
