import sqlite3 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # open the connection to the database
    conn = sqlite3.connect('crime_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    crimes = cur.execute("select * from crimes")
    department_id = crimes[0]['department_id']
    cur = conn.execute("select * from departments WHERE id=?", (department_id,))
    crimes = crimes.fetchall()
    departments = cur.fetchall()
    conn.close()
    return render_template('index.html', crimes=crimes, departments=departments)