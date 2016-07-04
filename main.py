import sys
from tornado.log import app_log as logger
from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from apps.registry import apps
from core.builder import Builder
from core.mongo import mongo_configurations

# Set runtime configurable settings via command line
define("port", default=8080, help="Set port to listen all requests")

def make_apps(settings, apps):
    """Application Management

    Here we register all apps and their routes.
    """
    return Application(apps.get_routes(), **settings)

if __name__ == "__main__":
    parse_command_line()
    build = Builder()

    try:

        logger.info('Initialize Typhoon...')
        configs = build.env('.env')
        build.logs(configs, logger)

        logger.info('Build settings...')
        logger.debug('Configs: %s', configs)

        # settings = build.settings(configs)

        # merge with motor settings
        # settings.update(motor = mongo_configurations(configs))

        # logger.debug('Settings: %s', settings)
        # logger.info('Running IOLoop...')

        # app = make_apps(settings, apps)
        # app.listen(options.port)
        #
        # IOLoop.current().start()

    except IOError:
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
