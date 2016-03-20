import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

import unittest
from mock import MagicMock
from core.builder import Builder

class FakeYamlObject(object):
    """Fake Yaml Object

    This object used as mocking yaml and add 'set'
    method to add key, value
    """

    props = {}

    def set(self, key, value):
        self.props[key] = value

    def get(self, key):
        self.props[key]

class TestTyphoon(unittest.TestCase):

    def test_build_env_mock_simple(self):
        """
        Test mock call Builder().env()
        """
        build = Builder()
        build.env = MagicMock(return_value='testing')
        env = build.env('env_test.yml', 'TEST')
        build.env.assert_called_with('env_test.yml', 'TEST')
        self.assertEqual('testing', env)

    def test_build_env_mock_fake_object(self):
        """
        Test mock call builder.env() and return yaml object
        """
        build = Builder()
        yaml = FakeYamlObject()
        yaml.set('key1', 'value1')
        yaml.set('key2', 'value2')

        build.env = MagicMock(return_value=yaml)
        env = build.env('env_test.yml', 'TEST')
        build.env.assert_called_with('env_test.yml', 'TEST')

        # test equal every key should same with yaml object values
        self.assertEqual(env, yaml)
        self.assertEqual(env.get('key1'), yaml.get('key1'))
        self.assertEqual(env.get('key2'), yaml.get('key2'))

        # test if key not exists
        with self.assertRaises(KeyError):
            env.get('key3')

    def test_build_env_wrong_real_env_file(self):
        """
        Test env should be trigger an exception when try to load
        wrong environment file
        """
        build = Builder()
        with self.assertRaises(IOError):
            build.env('env_test2.yml', 'TEST')

    def test_build_env_real_env_file(self):
        build = Builder()
        env = build.env('env_test.yml', env_name='TEST')
        self.assertEqual('VALUE1', env.get('KEY1'))
