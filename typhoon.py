import click
from core.cmd import builder, routes

@click.group()
def typhoon():
    """
    Main cli apps runner for Typhoon.  All core and apps commands should
    be listed here.
    """
    pass

if __name__ == '__main__':

    '''
    Add core cli apps here
    '''
    typhoon.add_command(builder.cli)
    typhoon.add_command(routes.cli)

    # run main cli apps
    typhoon()
