import click

@click.command('ping:ping')
def cli():
    """
    Just ping it
    """
    click.echo('pong')
