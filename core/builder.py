import uuid
import os
from dotenv import load_dotenv
from core.exceptions.core import UnknownEnvError, DotenvNotAvailableError

class Builder(object):

    def env(self, env_file):
        """Environment Management

        Previous implementation is using `mothernature` to manage
        our environment variables.  For now, i'm change it into
        python-dotenv that support with os environment variables.

        What we need to do here is we just need to load .env file,
        and python-dotenv will automatically will inject all key variables
        into os environment.

        Why we need to wrap this simple function into class method ? Because
        previous implementation has a logic inside this method, and i still
        to make it as class method, so if we have a changes in the future,
        we working on this method, not at the caller.

        Args:
            env_file (str): .env that need to load

        Raises:
            DotenvNotAvailableError : If cannot found any dotenv file
        """
        dotenv = load_dotenv(env_file)
        if not dotenv:
            raise DotenvNotAvailableError

    def settings(self, yaml):
        """Tornado Settings

        Build settings which will loaded by Tornado.  All configuration
        fetch from os environment variables.

        Current settings should be only for default global Tornado settings,
        like debug, cookie_secret and others.  It's should not handle any external
        settings like session or mongo settings.

        Returns:
            Dictionaries

        Raises:
            Raise a UnknownEnvError if cannot load main tornado settings based on current requested
            environment name
        """
        env_name = os.environ.get('ENV_NAME')
        env = yaml.get(env_name)

        if not env:
            raise UnknownEnvError(name=env_name)

        setting = {
            "debug": env.get('DEBUG'),
            "compress_response": env.get('COMPRESS_RESPONSE'),
            "cookie_secret": uuid.uuid1().hex,
            "xsrf_cookies": env.get('XSRF'),
            "static_hash_cache": env.get('STATIC_HASH_CACHE'),
            "static_path": os.environ.get('STATIC_PATH'),
            "static_url_prefix": os.environ.get('STATIC_URL_PREFIX')
        }

        return setting
