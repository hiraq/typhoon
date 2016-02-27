from abc import ABCMeta, abstractmethod

class Container(object):
    """Base Container Application

    This class should be used for each application and used to
    hold any information about registered app, such as for:
    - registered routes & handlers
    - define application name
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def routes(self):
        """
        Should be used for register any routes of app
        """
        pass

    @abstractmethod
    def name(self):
        """
        Should be used for define current application name
        """
        pass
