import sqlite3
from config import DB_NAME

DATABASE_FILE = DB_NAME

def initialize_database():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE codes (id INTEGER PRIMARY KEY, code TEXT)''')
    conn.commit()
    conn.close()


def add_code(code):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO codes (code) VALUES (?)", (code,))
    conn.commit()
    conn.close()


def get_codes():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM codes")
    codes = c.fetchall()
    conn.close()
    return codes


def delete_code(code):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM codes WHERE code = ?", (code,))
    conn.commit()
    conn.close()


# For first time setup, uncomment the next line:
# initialize_database()

