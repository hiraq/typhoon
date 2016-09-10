from tornado.web import Application as TornadoApp

class Application(TornadoApp):

    def __init__(self, routes, **settings):
        """
        Initialize tornado main Application.

        Args:
            routes : A list of touples contains route string and handler
        """
        TornadoApp.__init__(self, routes, **settings)
