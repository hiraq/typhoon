import click

@click.group()
def typhoon():
    """
    This is a main cli apps of Typhoon.  For now, there is only two
    sub commands available, they are:
    - builder: To create application skeleton
    - routes: To get all registered apps

    I just change the structure of typhoon's command line interfaces,
    and prepare this structure to support custom command line from inside
    app.
    """
    click.echo('hello')

@click.command('core:builder')
def builder():
    click.echo('cmd2')

@click.command('core:routes')
def routes():
    click.echo('cmd3')

if __name__ == '__main__':
    typhoon.add_command(builder)
    typhoon.add_command(routes)

    typhoon()
