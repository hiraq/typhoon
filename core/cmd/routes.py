import click

@click.command('core:routes')
def cli():
    """
    This core cli apps used to list all registered routes
    """
    click.echo('cmd3')
