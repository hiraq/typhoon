from collections import Iterator, Sized

class Router(Iterator, Sized):
    """Router Class

    This class used as DSL to build and register routes, and
    also add grouping endpoint functionality.

    Usage:

        # without grouping
        with Router(handler=MyHandlerClass) as routes:
            routes.register('/my_endpoint')

        # with grouping
        with Router(handler=MyHandlerClass, grouping='/prefix') as routes:
            routes.register('/my_endpoint')

    Attributes:
        self.routes = List of registered routes
        self.prefix = Used for grouping
        self.handler = Controller class
    """

    def __init__(self, group=None, handler=None):
        self.routes = list()
        self.prefix = group
        self.handler = handler

    def register(self, endpoint, name=None):
        """Register Route

        Used for register new endpoint

        Attributes:
            endpoint : A string endpoint path
        """
        endpoint = endpoint if not self.prefix else self.prefix + endpoint
        self.routes.append((endpoint, self.handler, name))

    def next(self):
        """Next Iteration

        This method used as implementation of Iteration

        Raises:
            StopIteration : Triggered when routes is empty
        """
        if not self.routes:
            raise StopIteration

        return self.routes.pop()

    def __len__(self):
        return len(self.routes)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass
