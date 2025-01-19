# https://www.youtube.com/watch?v=gOQCFPSjJ-8

from functools import wraps
from time import sleep
import typer
from typing import Annotated
import rich
from rich.progress import track

app = typer.Typer()

active_users = [
    'rob',
    'fab',
    'john'
]

admin_credentials = {'username': 'admin', 'password': 'password'}

def authenticated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        credentials = {k:v for k, v in kwargs.items() if k in 'username password'.split()}
        if credentials != admin_credentials:
            rich.print(f'[bold red]:locked_with_key: invalid credentials: {credentials}[/bold red]')
            exit(1)
        return func(*args, **kwargs)
    return wrapper


USERSLIST_TYPE = Annotated[list[str], typer.Argument(help='List of users')]
VERBOSE_TYPE = Annotated[bool, typer.Option(help='Show verbose output')]
USERNAME_TYPE = Annotated[str, typer.Option(help='your username', envvar='USER')]
PASSWORD_TYPE = Annotated[str, typer.Option(help='your password', envvar='PASSWORD',prompt=True, hide_input=True)]

@app.command()
@authenticated
def add_users(
    users:USERSLIST_TYPE,
    password:PASSWORD_TYPE,
    username:USERNAME_TYPE='admin',
    verbose:VERBOSE_TYPE=False,
):
    '''add users to the current users db'''
    for user in users:
        if verbose:
            print(f'user {user} added')
    print('add complete')


@app.command()
@authenticated
def delete_users(
    users:USERSLIST_TYPE, 
    password:PASSWORD_TYPE,
    username:USERNAME_TYPE='admin',
    verbose:VERBOSE_TYPE=False
):
    '''delete users from active db'''
    for user in users:
        if user not in active_users:
            # python -m rich.emoji
            rich.print(f'[bold yellow]:x: user {user} not in active db[/bold yellow]')
        else:
            if verbose:
                rich.print(f'[bold green]:white_heavy_check_mark: user {user} deleted[bold green]')
    print('deletion complete')


@app.command()
def list_users(
    verbose:VERBOSE_TYPE=False
):
    for user in track(active_users):
        sleep(.5)
        if verbose:
            rich.print(f'User: {user}')
    rich.print('done')


if __name__ == "__main__":
    app()
