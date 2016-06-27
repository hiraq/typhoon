from tornado.web import RequestHandler
from torndsession.session import SessionMixin

class BaseRequestHandler(RequestHandler, SessionMixin):
    """
    BaseRequestHandler should be used on any app class
    handler thant want to implement tornado RequestHandler
    and by default mixed with torndsession.session.SessionMixin
    to manage all session things.
    """

    def prepare(self):
        pass

    def on_finish(self):
        """
        Every request finished, torndsession will
        save session contents.
        """
        self.session.flush()
