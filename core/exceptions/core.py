class ContainerError(Exception):
    """Core.Exceptions.Application

    Custom exception to trigger an error when some
    application not implement Core.Container abstract
    class.
    """
    def __init__(self, app_name):

        self._message = "ContainerError: Cannot use {} as container application".format(app_name)
        self._app_name = app_name

        Exception.__init__(self, self._message)

    @property
    def app_name(self):
        return self._app_name    

    @property
    def message(self):
        return self._message
    