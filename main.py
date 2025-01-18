import typer

app = typer.Typer()

@app.command()
def add_users(users:list[str], verbose:bool=False):
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
