from tornado.web import RequestHandler
from apps.container import Container

class MainHandler(RequestHandler):
    def get(self):
        self.write('Hello World')

class HelloApp(Container):

    def routes(self):
        r = [(r"/hello", MainHandler)]
        return r

    def name(self):
        return "HelloApp"

app = HelloApp()
