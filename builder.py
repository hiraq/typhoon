import os
from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from helpers.cli import cement_log

class BuilderBaseController(CementBaseController):
    """Base builder controller

    Used to build cli skeleton for application builder
    """
    class Meta:
        label = 'base'
        description = 'Command Line Tools - Builder'
        arguments = [
            (['-a', '--app'], dict(action='store', help='Set application name to build'))
        ]

    @expose(hide=True)
    def default(self):
        """Build New Application Structure

        There are some steps to make it done.
        - We need to get current project directory
        - We need to set base application directory
        - We need to analyze if requested app exists or not.
        - If doesn't exists yet, then create the directory and basic empty files
        - If exists, then just stop the process
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        app_dir = current_dir + os.path.sep + 'apps' + os.path.sep

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

        def app_name():
            return self.app.pargs.app

        def build_file(path, name):
            """Implement Touch

            Create an empty file
            """
            filepath = path + name
            with open(filepath, 'a'):
                os.utime(filepath, None)

        # Analyze current states
        print '============================================================='
        cement_log(self).info('Current Directory: {}'.format(current_dir))
        cement_log(self).info('Application Directory: {}'.format(app_dir))
        print '============================================================='
        cement_log(self).info('Requested App Name: {}'.format(self.app.pargs.app))
        print '============================================================='

        if can_to_create_apps(app_dir, self.app.pargs.app):
            """
            Make recursive directory and also create a file is a sensitive process
            thaty may trigger an exception.  We should use try except method to catch
            any possible errors.  Any possible exceptions:
            - OSError
            - IOError
            - Exception
            """
            build_dir = app_dir + app_name() + os.path.sep

            try:
                os.makedirs(build_dir)

                """
                We need to create two basic files:
                - __init__.py to make current directory as python module
                - routes.py for application container
                """
                build_file(build_dir, '__init__.py')
                build_file(build_dir, 'routes.py')

                cement_log(self).info('Your application has been created.')
            except OSError as ose:
                cement_log(self).error('Cannot create directory due to: {}'.format(str(ose)))
            except IOError as ioe:
                cement_log(self).error('Cannot create any files due to: {}'.format(str(ioe)))
            except Exception as e:
                cement_log(self).error('Unknown error happened: {}.'.format(str(e)))
                raise

        else:
            # stop the process if application has been exists
            cement_log(self).error('Cannot create "{}" app, requested application has been exists'.format(app_name()))

class BuilderApp(CementApp):
    class Meta:
        label = 'builder'
        extensions = ['colorlog']
        log_handler = 'colorlog'
        base_controller = 'base'
        handlers = [BuilderBaseController]

with BuilderApp() as cli:
    cli.run()
