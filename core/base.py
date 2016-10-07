from tornado.web import RequestHandler
from tornado.log import app_log as logger
from torndsession.session import SessionMixin
from webargs.tornadoparser import parser

class BaseRequestHandler(RequestHandler, SessionMixin):
    """
    BaseRequestHandler should be used on any app class
    handler thant want to implement tornado RequestHandler
    and by default mixed with torndsession.session.SessionMixin
    to manage all session things.
    """

    def initialize(self):
        self.application.load_components(self)

    def on_finish(self):
        """
        Every request finished, torndsession will
        save session contents.
        """
        self.session.flush()

    def parse_request(self, args):
        """HTTP Request Parser

        Parse request parameters from any HTTP methods
        """
        return parser.parse(args, self.request)
