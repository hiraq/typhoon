import click
from core.cmd import builder, routes
from apps.registry import apps

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

    # We register all custom commands from each apps
    # if any commands registered.
    if len(apps.get_commands()) > 0:
        for command in apps.get_commands():
            typhoon.add_command(command)

    # run main cli apps
    typhoon()
