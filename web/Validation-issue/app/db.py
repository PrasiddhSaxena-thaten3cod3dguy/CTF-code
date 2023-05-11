import sqlite3
import hashlib

def connect():
    return sqlite3.connect("app/database.db")

def init_db():
    c = connect()
    with open("app/schema.sql", "r") as rf:
        c.executescript(rf.read())
    c.close()

def add_user(username, password):
    c = connect()
    c.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, hashlib.sha256(password.encode()).digest().hex()))
    c.commit()
    c.close()

def query_user(username):
    c = connect()
    return c.cursor().execute("SELECT username FROM users WHERE username=?", (username,)).fetchall()

def query_all(username):
    c = connect()
    return c.cursor().execute("SELECT username, password FROM users WHERE username=?", (username, )).fetchall()

def setup():
    init_db()
    add_user("admin", "mysupersecureelitepasswordnonecancrack31337")
