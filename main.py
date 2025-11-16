#! /usr/bin/python3

import click as ck
import string
import secrets
import sqlite3
import db

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

def make_psw(l: int) -> str:
    psw = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits)
    ]

    psw += [secrets.choice(string.ascii_letters + string.digits + "@$%^&*!><[]{}|") for _ in range(l - len(psw))]
    secrets.SystemRandom().shuffle(psw)

    return ''.join(psw)

db.init_store()
db.init_db(cursor)

@ck.group()
def cli():
    pass

@cli.command()
@ck.argument("app", type=ck.STRING)
@ck.argument("length", required = False)
def new_psw(app, length = 32):
    psw = make_psw(int(length))
    db.add_psw(conn, app, psw)

@cli.command()
def get_psw():
    l = db.get_psws(cursor)
    for x in l:
        ck.echo(f"{x[0]} | {x[1]}")

if __name__ == '__main__':
    cli()
