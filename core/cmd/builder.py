import os
import click

def build_apps_dir(current_dir):
    splitted = current_dir.split('/')
    splitted.remove('core')
    splitted.remove('cmd')

    sep = os.path.sep
    return '/'.join(splitted) +  sep + 'apps' + sep

def can_to_create_apps(app_dir,app_name):
    """Check Application Directory

    We list all directories inside application directory
    and make sure that current requested app is not exists.
    """
    for directory in os.listdir(app_dir):
        if os.path.isdir(app_dir + directory):
            if directory == app_name:
                return False
    return True

def build_file(path, name):
    """Implement Touch

    Create an empty file
    """
    filepath = path + name
    with open(filepath, 'a'):
        os.utime(filepath, None)

def build_app_name(app):
    return app.replace(' ','-').lower()

@click.command('core:builder')
@click.option('--app', default=None, help='Application name need to be set.')
def cli(app):
    """
    This core cli apps used to create skeleton apps
    """
    if not app:
        click.echo('You must set your app name')
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        apps_dir = build_apps_dir(current_dir)
        create_dir = apps_dir + build_app_name(app) + os.path.sep

        if can_to_create_apps(apps_dir, app):

            try:
                os.makedirs(create_dir)
                build_file(create_dir, '__init__.py')
                build_file(create_dir, 'routes.py')

                click.echo('Your app: {} has been created.'.format(app))
            except OSError, ose:
                click.echo('Cannot create directory for {}'.format(app))
            except IOError, ioe:
                click.echo('Cannot create any fiels for {}'.format(app))
            except Exception, e:
                click.echo('Unknown error has been raised for {}'.format(app))

        else:
            click.echo('Cannot create {}, this app has already exists.'.format(app))
