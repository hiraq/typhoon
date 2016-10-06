class BaseError(Exception):
    """Base Error Management

    All custom error exception should inherit from this
    class.  This base exception only handle error message.
    """

    def __init__(self):
        self._message = None

    @property
    def message(self):
        return self._message

class ContainerError(BaseError):
    """Error Container

    Custom exception to trigger an error when some
    application not implement Core.Container abstract
    class.
    """
    def __init__(self, app_name):
        BaseError.__init__(self)
        self._message = "ContainerError: Cannot use {} as container application".format(app_name)
        self._app_name = app_name

        Exception.__init__(self, self._message)

    @property
    def app_name(self):
        return self._app_name

class ComponentError(BaseError):
    """Error Component

    Should be triggered when cannot initialize component object,
    or given component object is not instance from Component abstract
    class.
    """
    def __init__(self, com_name):
        BaseError.__init__(self)
        self._message = "ComponentError: Cannot use {} as component object".format(com_name)

class DotenvNotAvailableError(BaseError):
    """Error Dotenv

    Custom exception should be triggered when
    dotenv file not found.
    """

    def __init__(self):
        BaseError.__init__(self)
        self._message = 'Unable to load environment file.'

class UnknownEnvError(BaseError):
    """Error Unknown Environment Name

    Custom exception that should be triggered when
    system try to load all environment variables from unspecified
    environment name.
    """
    def __init__(self, name=None):
        BaseError.__init__(self)
        self._message = 'Unknown environment name: {}.'.format(name)
