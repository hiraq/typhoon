import sys
import os
from os.path import dirname, abspath
from tornado.log import app_log as logger
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from apps.registry import apps
from core.application import Application as Typhoon
from core.builder import Builder
from core.environment import load_yaml_env
from core.setting import mongo, session
from core.exceptions.core import DotenvNotAvailableError, UnknownEnvError

# Set runtime configurable settings via command line
define("env", default=".env", help="Set default env file")
define("port", default=8080, help="Set port to listen all requests")
define("addr", default="localhost", help="Set ip address to listen")

'''
To run application we need to setup many things, they are :

- parse command line options
- initialize environment & settings builder
- initialize current root path project
- load environment variables from dotenv file, if not found then raise DotenvNotAvailableError
  exception
- load main tornado settings based on environment name variable found at environment variable
  (dotenv file)
- update settings, put root path
- update settings, put mongo
- update settings, put session
- load main tornado application, register all routes and settings
- set main port and address
- run IOLoop

For debugging process we also need to log any important flows above like environment variables
and main tornado configurations.

Two important exceptions that should be handled here are :

- DotenvNotAvailableError : When application cannot found any dotenv file
- UnknownEnvError : When application cannot load main tornado settings based on used environment name
  variable (DEV/STAGING/PRODUCTION)

It's better to use custom application class that extend from tornado.web.Application.  By this way,
we can set custom properties that can accessed from any base handler class.

Our challenges are :

- We have to make sure any exceptions that should be triggered can handled properly
- If any exceptions triggered, we doesn't need to continue the process, just stop other processes.
- Every important flows should be logged properly, we need to know about current state, when application
  initialize typhoon engine.
- Make clean main flows, all flows should can be read and understand easily

What we need to do:

- First we have to create custom Typhoon Application class that extend from tornado.web.Application.
- When we initialize object from this class, we just register all routes and main tornado settings.

'''

if __name__ == "__main__":

    parse_command_line()
    build = Builder()

    root_path = dirname(abspath(__file__))
    yaml = load_yaml_env('env.yaml')

    logger.info('Initialize Typhoon...')
    logger.debug('Env filepath: {}'.format(root_path + '/' + options.env))
    logger.debug('YAML objects : {}'.format(yaml))

    try:

        # build.env will raise DotenvNotAvailableError if
        # cannot found any dotenv file
        build.env(root_path + '/' + options.env)
        logger.debug('Used environment : {}'.format(os.environ.get('ENV_NAME')))

        # We need to build our global settings based on current selected
        # ENV_NAME (DEV, TEST, STAGING, PRODUCTION)
        # Will raise UnknownEnvError if cannot load main configurations
        # based on unknown environment name
        settings = build.settings(yaml)

        # merge with session settings, session should be registered
        # at tornado global settings, so it can be parsed by session mixin
        # component.
        settings.update(session = session.settings())

        logger.debug('Settings: %s', settings)
        logger.info('Running IOLoop...')
        logger.info('Listening port: {}'.format(options.port))
        logger.info('Listening to address: {}'.format(options.addr))

        # Initialize Typhoon engine
        # register root_path and motor as object property
        typhoon = Typhoon(apps.get_routes(), **settings)
        setattr(typhoon, 'root_path', root_path)
        setattr(typhoon, 'motor', mongo.settings())

        typhoon.listen(options.port, options.addr)
        IOLoop.current().start()

    except DotenvNotAvailableError, exc:
        """
        Should be happened when core builder cannot load default dotenv file
        """
        print exc.message
        sys.exit()

    except UnknownEnvError, exc:
        """
        Should be happened when core builder try to load unregistered key from
        environment configuration file.
        """
        print exc.message
        sys.exit()
