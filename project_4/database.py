import sqlite3

# Connect database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
description TEXT,
amount REAL,
category TEXT
)
""")

conn.commit()
conn.close()