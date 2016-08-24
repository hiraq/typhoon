import sys
import os
from os.path import dirname, abspath
from tornado.log import app_log as logger
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from apps.registry import apps
from core.builder import Builder
from core.environment import load_yaml_env
from core.setting import mongo, session
from core.exceptions.core import DotenvNotAvailableError

# Set runtime configurable settings via command line
define("env", default=".env", help="Set default env file")
define("port", default=8080, help="Set port to listen all requests")
define("addr", default="localhost", help="Set ip address to listen")

def make_apps(settings, apps):
    """Application Management

    Here we register all apps and their routes.
    """
    return Application(apps.get_routes(), **settings)

if __name__ == "__main__":

    parse_command_line()
    build = Builder()

    try:

        yaml = load_yaml_env('env.yaml')
        root_path = dirname(abspath(__file__))

        logger.info('Initialize Typhoon...')
        logger.debug('Env filepath: {}'.format(root_path + '/' + options.env))

        configs = build.env(root_path + '/' + options.env)

        # raise an DotenvNotAvailableError if .env not found
        if not configs:
            raise DotenvNotAvailableError

        # We need to build our global settings based on current selected
        # ENV_NAME (DEV, TEST, STAGING, PRODUCTION)
        logger.info('Build settings...')
        settings = build.settings(yaml[os.environ.get('ENV_NAME')])

        # add root path to application settings
        settings.update(root_path = root_path)

        # merge with motor settings
        settings.update(motor = mongo.settings())

        # merge with session settings
        settings.update(session = session.settings())

        logger.debug('Settings: %s', settings)
        logger.info('Running IOLoop...')
        logger.info('Listening port: {}'.format(options.port))
        logger.info('Listening to address: {}'.format(options.addr))

        app = make_apps(settings, apps)
        app.listen(options.port, options.addr)

        IOLoop.current().start()

    except DotenvNotAvailableError:
        """
        Should be happened when core builder cannot load default dotenv file
        """
        print 'Unable to load environment file.'
        sys.exit()

    except KeyError:
        """
        Should be happened when core builder try to load unregistered key from
        environment configuration file.
        """
        print 'Unable to load configuration values.'
        sys.exit()
