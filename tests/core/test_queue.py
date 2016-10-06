import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

import unittest
import logging
from tornado.testing import AsyncTestCase, gen_test
from tornado.gen import coroutine, Return, sleep
from tornado.log import app_log as logger
from core.queue import TQueue

class TestCore(AsyncTestCase):

    @gen_test
    def test_queue(self):

        message = 'message'

        @coroutine
        def listener(item):
            self.assertEqual(message, item)
            raise Return(item)

        q = TQueue()
        q.put(message)
        self.assertTrue(q.is_item_exists())

        q.register_callback(listener)
        yield q.run()
        yield sleep(1)
