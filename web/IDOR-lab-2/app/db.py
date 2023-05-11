import sqlite3
import hashlib

def connect():
    return sqlite3.connect("app/database.db")

def init_db():
    conn  = connect()
    with open("app/schema.sql", "r") as rf:
        conn.executescript(rf.read())
    conn.close()

def add_user_with_id(id, username, password):
    conn = connect()
    conn.execute("INSERT INTO users(id, username, password) VALUES (?, ?, ?)", (id, username, hashlib.sha256(password.encode()).digest().hex()))
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = connect()
    conn.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, hashlib.sha256(password.encode()).digest().hex()))
    conn.commit()
    conn.close()

def check_user(username):
    conn = connect()
    return conn.cursor().execute("SELECT username FROM users WHERE username=?", (username,)).fetchall()

def query(username):
    conn = connect()
    return conn.cursor().execute("SELECT username, password FROM users WHERE username=?", (username, )).fetchall()

def query_id(id):
    conn = connect()
    return conn.cursor().execute("SELECT username FROM users WHERE id=?", (id, )).fetchall()

def setup():
    init_db()
    add_user_with_id(0, "admin", "MySup3rS3cur34dm1nP4$$w0rd31337")
    add_user_with_id(1, "nehal", "SuperSaiyanNehal31337")
    add_user_with_id(2, "yash", "yash")
    add_user_with_id(3, "samarth", "samarth")
    add_user_with_id(4, "priya", "priya")