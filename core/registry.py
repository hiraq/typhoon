from core.container import Container 

class Registry:
    """Core.Registry

    This class used to handle all registered apps.
    All apps should be implement Core.Container abstract class
    """

    def __init__(self):
        self.__apps = []
        self.__routes = []

    def register(self, app):
        """Register application

        Each app should be an instance of Container abstract class

        Args:
            self (Core.Registry): Current object instance
            app (Core.Container): App class
        """

        # We have to make sure if current app implement Core.Container
        assert isinstance(app, Container), "All app should be implement Core.Container abstract class."

        # Register application        
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
