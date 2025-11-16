import sqlite3
import os

def init_store():
    if not os.path.isfile("store.db"):
        with open("store.db", "a") as _:
            pass

def init_db(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS passwords (\
        App VARCHAR(255) PRIMARY KEY,\
        Password VARCHAR(255) NOT NULL\
    );\
    ")

def add_psw(conn, app, psw):
    cur = conn.cursor()
    cur.execute(f"\
        INSERT INTO passwords (App, Password)\
        VALUES ('{app}', '{psw}');\
    ")
    conn.commit()

def get_psws(cur):
    res = cur.execute("SELECT App, Password FROM passwords;")
    return res.fetchall()
