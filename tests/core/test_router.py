import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

import unittest
import logging

from core.router import Router

class TestRouter(unittest.TestCase):

    def test_empty_routes(self):
        r = Router()
        self.assertTrue(len(r) == 0)

        with self.assertRaises(StopIteration):
            r.next()

    def test_set_route_no_group(self):

        with Router() as routes:
            routes.register('/test1')

        self.assertTrue(len(routes) == 1)

        for route in routes:
            self.assertEqual('/test1', route[0])
            self.assertEqual(None, route[1])

    def test_set_route_grouping(self):

        with Router(group='/prefix') as routes:
            routes.register('/test1')

        for route in routes:
            self.assertEqual('/prefix/test1', route[0])
