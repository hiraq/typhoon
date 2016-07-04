import uuid
import logging
from core.session import Session
from mothernature import Environment
from colorlog import ColoredFormatter

class Builder(object):

    def env(self, env_file):
        """Environment Management

        We should load all configuration based on current environment mode.
        Thanks to mothernature -> https://github.com/femmerling/mothernature

        Args:
            self (Builder): Current object instance
            env_file (str): Yaml file that need to load
            env_name (Optional[str]): Environment name that needed to load on
                initialize engine.  By default is DEV.

        Returns:
            Yaml object

        Raises:
            IOError: If given yaml file not found
        """
        env = Environment(env_file, env_name)
        config = env.get_config()
        return config

    def settings(self, config):
        """Tornado Settings

        Build settings which will loaded by Tornado.

        Args:
            self (Builder): Current object instance
            configs (yaml): Yaml object used to load environment variables

        Returns:
            Dictionaries
        """

        # build session configurations
        session = Session(config)
        session_settings = session.get_used_config()

        setting = {
            "debug": config.get('DEBUG'),
            "compress_response": config.get('COMPRESS_RESPONSE'),
            "cookie_secret": uuid.uuid1().hex,
            "xsrf_cookies": config.get('XSRF'),
            "static_hash_cache": config.get('STATIC_HASH_CACHE'),
            "static_path": config.get('STATIC_PATH'),
            "static_url_prefix": config.get('STATIC_URL_PREFIX')
        }

        # We doesn't need to add session settings if current
        # lifecycle just give us an empty dictionary
        if len(session_settings.keys()) > 0:
            setting.update(session = session_settings)

        return setting

    def logs(self, configs, logger):
        """Set Logging Level

        Use internal Tornado's logging helper.

        Args:
            self (Builder): Current object instance
            configs (yaml): Yaml object used to load environment variables
            logger (callback): Logger function
        """
        levels = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'ERROR': logging.ERROR,
            'WARNING': logging.WARNING,
            'CRITICAL': logging.CRITICAL
        }

        # Set default logging to logging info
        log_level = logging.INFO
        log_level_config = configs.get('LOG_LEVEL')

        # Set if log_level_config available on
        # registered levels
        if log_level_config in levels:
            log_level = levels[log_level_config]

        # Reset logging level
        logger.setLevel(log_level)
