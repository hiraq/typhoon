from core.base import BaseRequestHandler
from core.container import Container
from .commands import hello

class MainHandler(BaseRequestHandler):
    def get(self):
        self.write('Hello World')

class HelloApp(Container):

    @property
    def commands(self):
        return [hello.cli]

    def routes(self):
        routes = [(r"/hello", MainHandler)]
        return routes

    def name(self):
        return "HelloApp"

app = HelloApp()
