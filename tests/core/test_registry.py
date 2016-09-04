import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

import unittest
import logging

from types import *
from mock import MagicMock
from core.registry import Registry
from core.container import Container
from core.exceptions.core import ContainerError

def test_cli():
    pass

class FakeHandler(object):
    pass

class FakeApp1(Container):

    @property
    def commands(self):
        return [test_cli]

    def routes(self):
        routes = [(r"/testing1", FakeHandler)]
        return routes

    def name(self):
        return "FakeApp1"

class FakeApp2(Container):

    @property
    def commands(self):
        return []

    def routes(self):
        routes = [(r"/testing2", FakeHandler)]
        return routes

    def name(self):
        return "FakeApp2"

class FakeApp3(object):
    """
    This class used to test exception
    """
    pass

class FakeApp4(Container):

    @property
    def commands(self):
        return []

    def routes(self):
        routes = [(r"/testing3", FakeHandler, "testing")]
        return routes

    def name(self):
        return "FakeApp4"

class TestRegistry(unittest.TestCase):

    def test_build_registry(self):

        reg = Registry()
        reg.register(FakeApp1())
        reg.register(FakeApp2())
        reg.register(FakeApp4())

        # check if list of apps is not empty list
        self.assertIsNot(reg.get_apps(), [])
        self.assertEqual(3, len(reg.get_apps()))
        self.assertEqual(3, len(reg.get_routes()))

    def test_container_error(self):

        # test if application not implement container abstract class
        with self.assertRaises(ContainerError) as container_error:
            reg = Registry()
            reg.register(FakeApp3())

        exception = container_error.exception
        self.assertEqual('FakeApp3', exception.app_name)
        self.assertEqual('ContainerError: Cannot use FakeApp3 as container application', exception.message)

    def test_container_get_commands(self):

        reg = Registry()
        reg.register(FakeApp1())
        reg.register(FakeApp2())

        commands = reg.get_commands()
        self.assertTrue(len(commands) > 0)

    def test_container_get_commands_empty(self):

        reg = Registry()
        reg.register(FakeApp2())

        commands = reg.get_commands()
        self.assertFalse(len(commands) > 0)
