import os

class Session(object):

    def __init__(self, config):
        self.config = config

    def get_used_config(self):
        """Get Supported Session Configurations

        Current we just support redis and memcache as main
        session storage engines.

        Args:
            self: Current Session object

        Returns:
            A dictionary that filled with all session configuration
            key and values based on their session engines, or maybe
            just an empty dictionary if current choosen engine not
            supported yet.
        """
        if self.config['SESSION_ENGINE'] == 'REDIS':
            return self.__get_redis_config()
        elif self.config['SESSION_ENGINE'] == 'MEMCACHE':
            return self.__get_memcache_config()
        else:
            return dict()

    def __get_memcache_config(self):
        """Build Memcache Configurations

        Args:
            self: Current Memcache object

        Returns:
            A dictionary contains of memcache host and port
            configurations

        """
        return dict(
            driver = 'memcached',
            driver_settings = dict(
                host = self.config['SESSION_MEMCACHE_HOST'],
                port = self.config['SESSION_MEMCACHE_PORT']
            )
        )

    def __get_redis_config(self):
        """Build Redis Configurations

        Args:
            self: Current Session object

        Returns:
            A dictionary that filled with session driver and
            all redis related configurations.

        """

        """
        It's because max_connections is a optional
        setting, so we need to check it first before
        we build our redis configurations
        """
        if 'SESSION_REDIS_MAX_CONNECTIONS' in self.config:
            max_conn = self.config['SESSION_REDIS_MAX_CONNECTIONS']
        else:
            max_conn = 1024

        """
        Password field is also optional key.  So
        we need to make sure if current environment
        has that key or not, and if not just set it
        to None.
        """
        if 'SESSION_REDIS_PASSWORD' in self.config:
            password = self.config['SESSION_REDIS_PASSWORD']
        else:
            password = None

        session_settings = dict(
            driver = 'redis',
            driver_settings = dict(
                host = self.config['SESSION_REDIS_HOST'],
                port = self.config['SESSION_REDIS_PORT'],
                db = self.config['SESSION_REDIS_DB'],
                max_connections = max_conn,
                password = password
            )
        )

        return session_settings

def settings():
    session = Session(os.environ)
    return session.get_used_config()
