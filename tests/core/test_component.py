import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

import unittest
import logging

from core.component import Component as ComponentAbstract
from core.exceptions.core import ComponentError

class FakeComponent(ComponentAbstract):

    def install(self):
        pass

    def initialize(self):
        pass

class FakeComponentNotImplement(object):

    def __init__(self):
        logging.debug("fake component not implemented")

def _not_implemented(object):
    if not isinstance(object, ComponentAbstract):
        raise ComponentError(object.__class__.__name__)

    logging.debug(object.__class__.__name__)
    return False

class TestComponentAbstract(unittest.TestCase):

    def test_raise_component_error(self):
        fc = FakeComponentNotImplement()
        with self.assertRaises(ComponentError):
            _not_implemented(fc)

    def test_implement_component(self):
        fc = FakeComponent()
        self.assertFalse(_not_implemented(fc))
