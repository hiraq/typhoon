import sys
from mothernature import Environment
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from apps.registry import apps
from core.builder import Builder

# Set runtime configurable settings via command line
define("env", default="DEV", help="Set current environment mode")
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

        configs = build.env('.env', env_name=options.env)
        settings = build.settings(configs)
        app = make_apps(settings, apps)
        app.listen(options.port)

        IOLoop.current().start()

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
