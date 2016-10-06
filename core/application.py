from tornado.web import Application as TornadoApp
from core.component import Component as ComponentAbstract
from core.exceptions.core import ContainerError

class Application(TornadoApp):
    """Typhoon Core Application

    This class extend functionalities from tornado.web.Application.
    It means, every methods and properties inside this class accessible
    from any request handlers.

    Please do not access any of these forbidden methods from your request
    handlers :

    - __init__
    - install
    """

    def __init__(self, routes, **settings):
        """
        Initialize tornado main Application.

        Args:
            routes : A list of touples contains route string and handler
        """
        TornadoApp.__init__(self, routes, **settings)

        # initialize empty list of components
        # this variable used to save any registered component
        self.__components = []

    def install(self, component, alias):
        """Install Component Object

        This method used to install components,
        put component object into self.components.

        Before we register this component, we should
        trigger component's install method.

        All registered should be instance of Component
        abstract class.

        This method should only be called from main.py not
        from inside the handler.

        Args:
            component: Component object
            alias: A string used as property to access the component when initialize request

        Raises:
            ContainerError: When given component object is not an instance of
            component abstract class.
        """

        # check if given component object is an instance of Component
        # abstract class or not
        if not isinstance(component, ComponentAbstract):
            raise ContainerError(component.__class__.__name__)

        # install the component and register it into
        # self.components
        component.install()
        self.__components.append({alias: component})
