import pprint
from tornado import gen
from core.base import BaseRequestHandler
from core.container import Container

class MongoHandler(BaseRequestHandler):

    def initialize(self):
        self.motor = self.settings['motor']
        self.db = self.motor.testing_db
        self.coll = self.db.testing_coll

    @gen.coroutine
    def get(self):
        docs = yield self.coll.find_one({'email': 'test@test.com'})
        pprint.pprint(docs)

        self.write('Email: {}'.format(docs['email']))
        self.write("\n")
        self.write('ObjectID: {}'.format(str(docs['_id'])))
        self.write("\n")
        self.finish()

    @gen.coroutine
    def post(self):
        future = self.coll.insert({'email': 'test@test.com'})
        result = yield future
        pprint.pprint(result)

        self.write('ObjectID: {}'.format(str(result)))
        self.write("\n")
        self.finish()

class MongoApp(Container):

    def routes(self):
        routes = [(r"/mongo", MongoHandler, "GET")]
        return routes

    def name(self):
        return "MongoApp"

app = MongoApp()
