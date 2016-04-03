import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

import unittest
import logging

from types import *
from mock import MagicMock
from core.registry import Registry
from core.container import Container
from core.exceptions.application import ContainerError

class FakeHandler(object):
    pass

class FakeApp1(Container):
    def routes(self):
        routes = [(r"/testing1", FakeHandler, "GET")]
        return routes

    def name(self):
        return "FakeApp1"

class FakeApp2(Container):
    def routes(self):
        routes = [(r"/testing2", FakeHandler, "GET")]
        return routes

    def name(self):
        return "FakeApp2"

class FakeApp3(object):
    """
    This class used to test exception
    """
    pass

class TestRegistry(unittest.TestCase):

    def test_build_registry(self):

        reg = Registry()
        reg.register(FakeApp1())
        reg.register(FakeApp2())

        # check if list of apps is not empty list
        self.assertIsNot(reg.get_apps(), [])
        self.assertEqual(2, len(reg.get_apps()))
        self.assertEqual(2, len(reg.get_routes()))

    def test_container_error(self):

        # test if application not implement container abstract class
        with self.assertRaises(ContainerError):
            reg = Registry()
            reg.register(FakeApp3())