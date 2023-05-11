import sqlite3
import hashlib

def connect_db():
    return sqlite3.connect("app/database.db")

def init_db():
    with open("app/schema.sql", "r") as rf:
        script = rf.read()
    conn = connect_db()
    conn.executescript(script)
    conn.close()

def add_data(username, password, url):
    conn = connect_db()
    conn.cursor().execute("INSERT INTO users (username, password, url) VALUES (?, ?, ?)", (username, hashlib.sha256(password.encode()).digest().hex(), url))
    conn.commit()
    conn.close()

def query_username(username):
    conn = connect_db()
    return conn.execute("SELECT username FROM users WHERE username=?", (username,)).fetchall()

def query_all(username):
    conn = connect_db()
    return conn.execute("SELECT username, password, url FROM users WHERE username=?", (username, )).fetchall()

def setup():
    init_db()
    add_data("admin", "password", "app/static/uploads/DmzRDZfajD.png")