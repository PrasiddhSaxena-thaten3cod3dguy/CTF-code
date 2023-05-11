import sqlite3
import random
import string

def connect():
    return sqlite3.connect("users.db")

def runschema():
    with open("schema.sql", "r") as rf:
        c = connect()
        c.executescript(rf.read())
        c.close()

def add_user(username, password):
    c = connect()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    c.commit()
    c.close()

def query(username):
    c = connect()
    return c.cursor().execute("SELECT username, password FROM users WHERE username='"+ username + "'").fetchall()

def query_secure(username):
    c = connect()
    return c.cursor().execute("SELECT username, password FROM users WHERE username=?", (username,)).fetchall()

def setup_db():
    runschema()
    #add_user("admin", "".join([random.choice(string.ascii_letters + string.digits) for _ in range(32)]))
    add_user("admin", "Hackershala@ae4b2227218c75ab513bb0043640dc4d31337")

if __name__ == "__main__":
    setup_db()