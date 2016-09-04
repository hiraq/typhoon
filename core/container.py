from abc import ABCMeta, abstractmethod, abstractproperty

class Container:
    """Base Container Application

    This class should be used for each application and used to
    hold any information about registered app, such as for:
    - registered routes & handlers
    - define application name
    """
    __metaclass__ = ABCMeta

    @abstractproperty
    def commands(self):
        """
        Should be used to list all custom cli commands from
        each apps.  This method should return a list of function
        that registered with click.

        If current registered apps, doesn't need any custom cli commands,
        just return an empty list.
        """
        pass

    @abstractmethod
    def routes(self):
        """
        Should be used for register any routes of app and return
        a list of tuple that contain route url (required), handler (required)
        and route name (optional)
        """
        pass

    @abstractmethod
    def name(self):
        """
        Should be used for define current application name
        """
        pass
