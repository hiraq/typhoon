from core.base import BaseRequestHandler
from core.container import Container

class MainHandler(BaseRequestHandler):
    def get(self):
        self.write('Hello World')

class HelloApp(Container):

    def routes(self):
        routes = [(r"/hello", MainHandler, "GET")]
        return routes

    def name(self):
        return "HelloApp"

app = HelloApp()
