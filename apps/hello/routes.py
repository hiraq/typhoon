from tornado.web import RequestHandler
from apps.container import Container

class MainHandler(RequestHandler):
    def get(self):
        self.write('Hello World')

class HelloApp(Container):

    def routes(self):
        routes = [(r"/hello", MainHandler, "GET")]
        return routes

    def name(self):
        return "HelloApp"

app = HelloApp()
