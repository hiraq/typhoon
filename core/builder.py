import uuid
from mothernature import Environment

class Builder(object):

    def env(self, env_file, env_name="DEV"):
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
        setting = {
            "debug": config.get('DEBUG'),
            "compress_response": config.get('COMPRESS_RESPONSE'),
            "cookie_secret": uuid.uuid1().hex,
            "xsrf_cookies": config.get('XSRF'),
            "static_hash_cache": config.get('STATIC_HASH_CACHE'),
            "static_path": config.get('STATIC_PATH'),
            "static_url_prefix": config.get('STATIC_URL_PREFIX') 
        }

        return setting
