import click

@click.command('ping:pong')
def cli():
    """
    Just pong it
    """
    click.echo('ping')
