import typer
from typing import Annotated

app = typer.Typer()

USERSLIST_TYPE = Annotated[list[str], typer.Argument(help='List of users')]
VERBOSE_TYPE = Annotated[bool, typer.Option(help='Show verbose output')]

@app.command()
def add_users(users:USERSLIST_TYPE, verbose:VERBOSE_TYPE=False):
    '''add users to the current users db'''
    for user in users:
        if verbose:
            print(f'user {user} added')
    print('add complete')

@app.command()
def delete_users():
    pass


@app.command()
def list_users():
    pass


if __name__ == "__main__":
    app()
