from tornado.web import RequestHandler

class PingHandler(RequestHandler):
    def get(self):
        self.write('pong')

routes = [(r"/ping", PingHandler)]
