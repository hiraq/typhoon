import click

@click.command('hello:hello')
def cli():
    """
    This cli apps used to give an example creating
    custom command from apps
    """
    click.echo('hello world')
