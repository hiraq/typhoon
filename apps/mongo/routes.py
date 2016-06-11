from core.base import BaseRequestHandler
from core.container import Container

class MongoHandler(BaseRequestHandler):
    def get(self):
        db = self.settings['motor']
        self.write(db.__class__.__name__)

class MongoApp(Container):

    def routes(self):
        routes = [(r"/mongo", MongoHandler, "GET")]
        return routes

    def name(self):
        return "MongoApp"

app = MongoApp()
