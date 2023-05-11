import sqlite3
import hashlib

def connect():
    return sqlite3.connect("app/database.db")

def init():
    c = connect()
    with open("app/schema.sql", "r") as schema:
        c.executescript(schema.read())

def add_user(username, password):
    c = connect()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    c.commit()
    c.close()

def query(username):
    c = connect()
    return c.cursor().execute("SELECT username, password FROM users WHERE username='" + username + "'").fetchall()

def query_secure(username):
    c = connect()
    return c.cursor().execute("SELECT username, password FROM users WHERE username=?", (username,)).fetchall()


def setup():
    init()
    add_user("admin_vhnreiug", "1fY0uF0undM3Y0u4r30nTh3R1ghtTr4ck31337")

if __name__ == "__main__":
    setup()
    print(query("admin"))
