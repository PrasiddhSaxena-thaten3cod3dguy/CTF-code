import sqlite3

def connect():
    return sqlite3.connect("database.db")

def runschema():
    with open("schema.sql", "r") as schema:
        c = connect()
        c.executescript(schema.read())

def add_user():
    c = connect()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin_cbushdf", "chueuwfybu834yw5r983409ifcushiebufouisawe"))
    c.commit()
    c.close()

def query(username):
    c = connect()
    output = c.cursor().execute("SELECT username,password FROM users WHERE username='" + username + "'").fetchall()
    return output

def query_secure(username):
    c = connect()
    output = c.cursor().execute("SELECT username, password FROM users WHERE username=?", (username,)).fetchall()
    return output

def setup():
    runschema()
    add_user()