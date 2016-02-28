from apps.hello.routes import app as HelloApp
from apps.ping.routes import app as PingApp

class Registry:

    def __init__(self):
        self.__apps = []
        self.__routes = []

    def register(self, app):
        """Register application

        Each app should be an instance of Container abstract class
        """
        self.__apps.append(app)

        # after app registered, we should parse their routes
        self.__app_routes()

    def __app_routes(self):
        """Binding routes

        We should load all registered app routes here.
        """
        for app in self.__apps:
            routes = app.routes()
            for route in routes:
                data = [(route[0], route[1])]
                self.__routes.extend(data)

    def get_apps(self):
        return self.__apps

    def get_routes(self):
        return self.__routes

"""
You should register all of your apps here.
"""
apps = Registry()
apps.register(HelloApp)
apps.register(PingApp)
