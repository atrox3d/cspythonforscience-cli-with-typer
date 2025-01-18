import typer

app = typer.Typer()

@app.command()
def add_users():
    pass


@app.command()
def delete_users():
    pass


@app.command()
def list_users():
    pass


if __name__ == "__main__":
    app()
