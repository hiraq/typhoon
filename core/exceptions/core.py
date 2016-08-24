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

class DotenvNotAvailableError(BaseError):
    """Error Dotenv

    Custom exception should be triggered when
    dotenv file not found.
    """

    def __init__(self):
        BaseError.__init__(self)
        self._message = 'Unable to load environment file.'
