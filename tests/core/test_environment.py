import sys
import os
from os.path import dirname, abspath
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

import unittest
import logging
import yaml

from types import *
from mock import MagicMock, mock_open, patch
from core.environment import load_yaml_env
from core.exceptions.core import ContainerError

class TestEnvironment(unittest.TestCase):

    def setUp(self):
        self.__test_path = dirname(abspath(__file__))

    def test_not_found(self):
        yaml = load_yaml_env('fake_path')
        self.assertTrue(len(yaml) < 1)

    @patch('core.environment.yaml')
    def test_read_yaml(self, mock_yaml):
        mock_yaml.load = MagicMock()
        mock_yaml.load.return_value = dict(test='testing')

        m = mock_open()
        with patch('core.environment.open', m, create=True):
            yaml = load_yaml_env('fake_path')

        m.assert_called_with('fake_path', 'r')
        self.assertTrue(len(yaml) > 0)
        self.assertEqual(yaml['test'], 'testing')

    @patch('core.environment.yaml')
    def test_yaml_error(self, mock_yaml):

        def _raise_yaml_error(*args):
            raise yaml.YAMLError

        mock_yaml.load = MagicMock()
        mock_yaml.load.side_effect = _raise_yaml_error

        m = mock_open()
        with patch('core.environment.open', m, create=True):
            yaml_dict = load_yaml_env('fake_path')
            self.assertTrue(len(yaml_dict) < 1)

        m.assert_called_with('fake_path', 'r')
