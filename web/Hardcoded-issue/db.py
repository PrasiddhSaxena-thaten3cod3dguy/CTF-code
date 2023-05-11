import random
import string
import sqlite3
import hashlib

def connect_db():
    return sqlite3.connect("database.db")

def init_db():
    with open("schema.sql", "r") as rf:
        conn = connect_db()
        conn.executescript(rf.read())
        conn.close()

def add_user(username, password):
    conn = connect_db()
    conn.cursor().execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, hashlib.sha256(password.encode()).digest().hex()))
    conn.commit()
    conn.close()

def query_login(username):
    conn = connect_db()
    return conn.execute("SELECT username, password FROM users WHERE username=?", (username,)).fetchall()

def setup_db():
    init_db()
    add_user("admin", "".join(random.choice(string.ascii_letters) for _ in range(20)))
    # YOU CAN NOT HACK ME IF MY PASSWORD IS RANDOM :P