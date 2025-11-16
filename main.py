#! /usr/bin/python3

from typing import Type
import click as ck
import random as rnd
import string
import secrets

def make_pass(l: int = 32) -> str:
    psw = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits)
    ]

    psw += [secrets.choice(string.ascii_letters + string.digits) for _ in range(l - len(psw))]
    secrets.SystemRandom().shuffle(psw)

    return ''.join(psw)



@ck.command()
@ck.argument("length")
def cli(length):
    ck.echo(make_pass(int(length)))

if __name__ == '__main__':
    cli()
