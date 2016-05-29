class Session(object):

    def __init__(self, config):
        self.engine = config.get('SESSION_ENGINE')
        self.env_settings = config.get('SESSION_DRIVERS')

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
        if self.engine == 'REDIS':
            return self.__get_redis_config()
        elif self.engine == 'MEMCACHE':
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
        memcache_env = self.env_settings['MEMCACHE']
        return dict(
            driver = 'memcached',
            driver_settings = dict(
                host = memcache_env['HOST'],
                port = memcache_env['PORT']
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
        redis_env = self.env_settings['REDIS']

        """
        It's because max_connections is a optional
        setting, so we need to check it first before
        we build our redis configurations
        """
        if 'MAX_CONNECTIONS' in redis_env:
            max_conn = redis_env['MAX_CONNECTIONS']
        else:
            max_conn = 1024

        """
        Password field is also optional key.  So
        we need to make sure if current environment
        has that key or not, and if not just set it
        to None.
        """
        if 'PASSWORD' in redis_env:
            password = redis_env['PASSWORD']
        else:
            password = None

        session_settings = dict(
            driver = 'redis',
            driver_settings = dict(
                host = redis_env['HOST'],
                port = redis_env['PORT'],
                db = redis_env['DB'],
                max_connections = max_conn,
                password = password
            )
        )

        return session_settings
