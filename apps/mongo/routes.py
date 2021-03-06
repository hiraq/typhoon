import pprint
from tornado import gen
from tornado.log import app_log as logger
from core.base import BaseRequestHandler
from core.container import Container
from core.router import Router
from webargs import fields
from tornado.log import app_log as logger

class MongoHandler(BaseRequestHandler):

    mongo_handler_args = {
        'email': fields.Email(required=True)
    }

    def initialize(self):
        super(MongoHandler, self).initialize()
        self.motor = self.mongo
        self.db = self.motor.testing_db
        self.coll = self.db.testing_coll

    @gen.coroutine
    def get(self):
        reqargs = self.parse_request(self.mongo_handler_args)
        docs = yield self.coll.find_one({'email': reqargs['email']})
        pprint.pprint(docs)

        if not docs:
            response = dict()
        else:
            response = dict(
                object_id = str(docs['_id']),
                email = docs['email']
            )

        self.write(response)
        self.finish()

    @gen.coroutine
    def post(self):
        reqargs = self.parse_request(self.mongo_handler_args)
        future = self.coll.insert({'email': reqargs['email']})
        result = yield future

        response = dict(
            object_id = str(result)
        )

        self.write(response)
        self.finish()

class MongoApp(Container):

    @property
    def commands(self):
        return []

    def routes(self):
        with Router(handler=MongoHandler) as routes:
            routes.register(r"/mongo", name='mongo_url')

        return routes

    def name(self):
        return "MongoApp"

app = MongoApp()
