from abc import ABCMeta, abstractmethod

class Component:
    """Base Component

    This abstract class should be implemented by
    all component classes.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def install(self):
        """Install Procedure

        This method will be called when Typhoon registered
        to Application global object.

        If current component doesn't need any installation process
        just pass it.

        This method should not return or raise anything (void)

        Returns:
            Void
        """
        pass

    @abstractmethod
    def initialize(self):
        """Initialize On Request

        This method will be called at initialize base request.

        If current component doesn't need any initialization process
        just pass it.

        Returns:
            Void or some objects
        """
        pass
