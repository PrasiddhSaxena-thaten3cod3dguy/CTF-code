import sqlite3
import hashlib

def connect_db():
    return sqlite3.connect("Application/database.db")

def init_db():
    conn = connect_db()
    with open("Application/schema.sql") as f:
        conn.executescript(f.read())

def add_flag():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO flag(flag) VALUES (?)", ("HACKERSHALA{SQL_1nj3ct10n_f0r_da_w1n}",))
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users(username, password) VALUES (?, ?)", (username, hashlib.sha256(password.encode()).digest().hex()))
    conn.commit()
    conn.close()

def query_username(username):
    conn = connect_db()
    cursor = conn.cursor()
    string = f"SELECT username FROM users WHERE username='{username}'"
    return cursor.execute(string).fetchall()

def query_username_secure(username):
    conn = connect_db()
    cursor = conn.cursor()
    string = "SELECT username FROM users WHERE username=?"
    return cursor.execute(string, (username,)).fetchall()

def query(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    string = f"SELECT username,password FROM users WHERE username=? AND password=?"
    return cursor.execute(string, (username, hashlib.sha256(password.encode()).digest().hex())).fetchall()

def setup():
    init_db()
    add_user("admin", "thereisnopointindumpingadminpasswordcauseitisofnouseandthisisaprettylongpassword")
    add_flag()