from tornado.web import RequestHandler
from apps.container import Container

class PingHandler(RequestHandler):
    def get(self):
        self.write('pong')

class PingApp(Container):

    def routes(self):
        routes = [(r"/ping", PingHandler)]
        return routes

    def name(self):
        return "PingApp"

app = PingApp()
