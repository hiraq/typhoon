import uuid
from mothernature import Environment
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from apps.registry import apps

# Set runtime configurable settings via command line
define("env", default="DEV", help="Set current environment mode")
define("port", default=8080, help="Set port to listen all requests")

def build_env():
    """Environment Management

    We should load all configuration based on current environment mode.
    Thanks to mothernature -> https://github.com/femmerling/mothernature
    """
    env = Environment("env.yml", options.env)
    config = env.get_config()
    return config

def build_settings(config):
    """Settings Management

    Should be used to configure all important keys.
    """
    return {
        "debug": config.get('DEBUG'),
        "compress_response": config.get('COMPRESS_RESPONSE'),
        "cookie_secret": uuid.uuid1().hex,
        "xsrf_cookies": config.get('XSRF'),
        "static_hash_cache": config.get('STATIC_HASH_CACHE'),
        "static_path": "assets",
        "static_url_prefix": "/statics/"
    }

def make_apps(settings, apps):
    """Application Management

    Here we register all apps and their routes.
    """
    return Application(apps.get_routes(), **settings)

if __name__ == "__main__":
    parse_command_line()
    settings = build_settings(build_env())

    app = make_apps(settings, apps)
    app.listen(options.port)

    IOLoop.current().start()
