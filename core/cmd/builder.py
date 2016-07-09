import click

@click.command('core:builder')
def cli():
    """
    This core cli apps used to create skeleton apps
    """
    click.echo('core:builder called')
