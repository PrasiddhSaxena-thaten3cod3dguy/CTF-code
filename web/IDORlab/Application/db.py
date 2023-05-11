import sqlite3
import hashlib

def connect_db():
    return sqlite3.connect("Application/database.db")

def init_db():
    with open("Application/schema.sql", "r") as cmd:
        conn = connect_db()
        conn.executescript(cmd.read())
        conn.close()

def add_user(username, password):
    conn = connect_db()
    conn.cursor().execute("INSERT INTO users(username,password) VALUES (?, ?)", (username, hashlib.sha256(password.encode()).digest().hex()))
    conn.commit()
    conn.close()

def query_user(username):
    conn = connect_db()
    return conn.cursor().execute("SELECT username FROM users WHERE username=?", (username,)).fetchall()

def query(username, password):
    conn = connect_db()
    return conn.cursor().execute("SELECT username,password FROM users WHERE username=? AND password=?", (username, hashlib.sha256(password.encode()).digest().hex())).fetchall()

def all_users():
    conn =connect_db()
    return conn.cursor().execute("SELECT id,username from users").fetchall()

def delete(id):
    conn = connect_db()
    conn.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()

def setup():
    conn = connect_db()
    init_db()
    add_user("admin", "MySuperSecureAdminPasswordNoOneCanCrackAsItIsTooLongToBeCracked1234567890")
    add_user("bulma", "Yamcha'sHotChick1234")
    add_user("trunks", "GotenksTheGodlySaiyan1234")