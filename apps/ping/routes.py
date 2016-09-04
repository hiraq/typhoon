from core.base import BaseRequestHandler
from core.container import Container
from .commands import ping, pong

class PingHandler(BaseRequestHandler):
    def get(self):
        self.write('pong')

class PongHandler(BaseRequestHandler):
    def get(self):
        self.write('ping')

class PingApp(Container):

    @property
    def commands(self):
        return [ping.cli, pong.cli]

    def routes(self):
        routes = [(r"/ping", PingHandler, "get_ping"), (r"/pong", PongHandler, "GET", "get_pong")]
        return routes

    def name(self):
        return "PingApp"

app = PingApp()
