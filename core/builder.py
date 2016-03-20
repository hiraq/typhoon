from mothernature import Environment

class Builder(object):

    def env(self, env_file, env_name="DEV"):
        """Environment Management

        We should load all configuration based on current environment mode.
        Thanks to mothernature -> https://github.com/femmerling/mothernature

        Args:
            self (Typhoon): Current object instance
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

    def settings(self):
        pass
