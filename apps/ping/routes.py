from core.base import BaseRequestHandler
from core.container import Container

class PingHandler(BaseRequestHandler):
    def get(self):
        self.write('pong')

class PongHandler(BaseRequestHandler):
    def get(self):
        self.write('ping')

class PingApp(Container):

    def routes(self):
        routes = [(r"/ping", PingHandler, "GET", "get_ping"), (r"/pong", PongHandler, "GET", "get_pong")]
        return routes

    def name(self):
        return "PingApp"

app = PingApp()
