import sys
import os
import json
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../../')

from tornado.testing import gen_test
from tornado.web import Application
from tornado.testing import AsyncHTTPTestCase
from motor.motor_tornado import MotorClient
from apps.mongo.routes import MongoHandler
from tornado.log import app_log as logger

def mongo_conn():
    # Use default host & port, just for testing
    return MotorClient()

def mongo_coll():
    mongo = mongo_conn()
    return mongo.testing_db.testing_coll

def make_app():

    app = Application([
        (r"/mongo", MongoHandler)
    ])

    app.motor = mongo_conn()
    return app

class TestRoutes(AsyncHTTPTestCase):

    def get_app(self):
        return make_app()

    def setUp(self):
        super(TestRoutes, self).setUp()
        mongo = mongo_conn()
        db = mongo.testing_db
        coll = db.testing_coll
        coll.remove()

    @gen_test
    def test_should_be_empty_for_now(self):
        mongo = mongo_conn()
        coll = mongo.testing_db.testing_coll
        total = yield coll.find().count()
        self.assertTrue(total < 1)

    def test_get(self):
        get = self.fetch('/mongo?email=test@test.com')
        response = json.loads(get.body)
        self.assertFalse(response)

    def test_post_then_get(self):

        payload = {
            'email': 'test@test.com'
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        coll = mongo_coll()
        post = self.fetch('/mongo', headers=headers, method="POST", body=json.dumps(payload))
        self.assertEqual(post.code, 200)
