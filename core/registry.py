import logging as logger
from core.container import Container 
from core.exceptions.application import ContainerError

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
        try:

            # We have to make sure if current app implement Core.Container
            # This assertions is important, we need to check all registered app
            assert isinstance(app, Container), "All app should be implement Core.Container abstract class."

            # Register application        
            self.__apps.append(app)

            # after app registered, we should parse their routes
            self.__app_routes()

        except AssertionError:

            # raise custom exception to indicate cannot use registered app
            raise ContainerError(app.__class__.__name__)

    def __app_routes(self):
        """Binding routes

        We should load all registered app routes here.
        """
        for app in self.__apps:
            routes = app.routes()
            for route in routes:

                """
                Tornado URLSpec depends on :
                - pattern
                - handler
                - kwargs (optional)
                - name (optional)

                Source: http://www.tornadoweb.org/en/stable/web.html#tornado.web.URLSpec

                Based on this documentation, we need to check if current registered route
                has a route name for reverse_url or not.

                kwargs act as additional arguments passed to handler constructor

                - route[0]: pattern
                - route[1]: handler
                - route[3]: route name

                Everything listed here, only used by tornado.Application.URLSpec.  I'm not
                use route[2] here, because route[2] used as additional information for http methods
                (GET, POST, PUT, DELETE) at routes.py command line interface.
                """
                if len(route) == 4:
                    data = [(route[0], route[1], None, route[3])]
                else:
                    data = [(route[0], route[1], None, None)]

                self.__routes.extend(data)

        # remove duplicate values from list of routes
        self.__routes = list(set(self.__routes))

    def get_apps(self):
        """Get all registered applications

        Returns:
            list of applications
        """
        return self.__apps

    def get_routes(self):
        """Get all parsed routes from all registered applications

        Returns:
            list of routes from many apps    
        """
        return self.__routes
