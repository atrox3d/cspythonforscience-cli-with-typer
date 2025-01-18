import typer
from typing import Annotated

app = typer.Typer()

active_users = [
    'rob',
    'fab',
    'john'
]

USERSLIST_TYPE = Annotated[list[str], typer.Argument(help='List of users')]
VERBOSE_TYPE = Annotated[bool, typer.Option(help='Show verbose output')]

@app.command()
def add_users(
    users:USERSLIST_TYPE, 
    verbose:VERBOSE_TYPE=False
):
    '''add users to the current users db'''
    for user in users:
        if verbose:
            print(f'user {user} added')
    print('add complete')


@app.command()
def delete_users(
    users:USERSLIST_TYPE, 
    verbose:VERBOSE_TYPE=False
):
    '''delete users from active db'''
    for user in users:
        if user not in active_users:
            print(f'user {user} not in active db')
        else:
            if verbose:
                print(f'user {user} deleted')
    print('deletion complete')


@app.command()
def list_users():
    pass


if __name__ == "__main__":
    app()
