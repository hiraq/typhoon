class Environment(object):
    """Environment Class

    This class should be used to manage all boolean or all value type
    except for string value for environment variables, and group it based on environment name
    such as :
    - DEV
    - TEST
    - STAGING
    - PRODUCTION
    """
    DEV = {
        "DEBUG": True,
        "XSRF": False,
        "STATIC_HASH_CACHE": False,
        "COMPRESS_RESPONSE": False
    }

    def __init__(self, env_name):

        if env_name == 'DEV':
            self.configs = self.DEV
        elif env_name == 'TEST':
            self.configs = self.TEST
        elif env_name == 'STAGING':
            self.configs = self.STAGING
        elif env_name == 'PRODUCTION':
            self.configs = self.PRODUCTION
        else:
            self.configs = dict()
