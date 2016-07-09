import click
from tabulate import tabulate
from apps.registry import apps

def build_routes(name, route):
    if len(route) == 3:
        return [name,route[0], route[1].__name__, route[2]]
    else:
        return [name,route[0], route[1].__name__, '-']


@click.command('core:routes')
def cli():
    """
    This core cli apps used to list all registered routes
    """
    data = []
    for app in apps.get_apps():
        routes = app.routes()
        for route in routes:
            data.append(build_routes(app.name(), route))

    headers = ['APPLICATION NAME','PATH', 'HANDLER', 'ROUTE NAME']
    table = tabulate(data, headers, tablefmt="psql")
    click.echo(table)
