import sqlite3

# Creates a new db opr just conencts to an exisiting one
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Creatin user table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()
conn.close()
