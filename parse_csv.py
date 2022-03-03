import csv
import sqlite3

from numpy import str0

# open the connection to the database crime
conn = sqlite3.connect('crime_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS crimes')
print("table dropped successfully");

conn.execute('DROP TABLE IF EXISTS departments')
print("table dropped successfully");

# create table again
conn.execute('CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT)')
print("table created successfully");

conn.execute('CREATE TABLE crimes (ORI_ID TEXT, YEAR TEXT, latitude REAL, longitude REAL, department_id INTEGER, total_pop REAL, homs_sum REAL, FOREIGN KEY(department_id) REFERENCES departments(id) )')
print("table created successfully");


with open('datasets/department.csv', newline='') as g:
    reader = csv.reader(g, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        id = int(row[0])
        name = str(row[1])

        cur.execute('INSERT INTO departments VALUES (?,?)', (id, name))
    print("data parsed successfully");
    conn.commit()

with open('datasets/crime.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        ORI_ID = str(row[0])
        YEAR = int(row[1])
        longitude = float(row[16])
        latitude = float(row[15])
        department_id = row[2]
        total_pop = row[3]
        homs_sum = row[4]

        cur.execute('INSERT INTO crimes VALUES (?,?,?,?,?,?,?)', (ORI_ID, YEAR, longitude, latitude, department_id, total_pop, homs_sum))
    print("data parsed successfully");
    conn.commit()
    conn.close()