import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

import unittest
import logging

from tornado.log import app_log as logger
from mock import MagicMock, patch
from core.builder import Builder
from core.exceptions.core import DotenvNotAvailableError, UnknownEnvError

def _test_dotenv(configs):
    if not configs:
        raise DotenvNotAvailableError

class FakeEnvironment(object):

    def __init__(self, keyval):
        self.configs = keyval

class TestBuilder(unittest.TestCase):

    @patch('core.builder.load_dotenv')
    def test_load_env_failed(self, load_dotenv):
        load_dotenv.return_value = None
        builder = Builder()

        self.assertIsNone(builder.env('testing'))

        with self.assertRaises(DotenvNotAvailableError):
            _test_dotenv(builder.env('testing'))

    @patch('core.builder.load_dotenv')
    def test_load_env_success(self, load_dotenv):
        load_dotenv.return_value = True
        builder = Builder()

        self.assertTrue(builder.env('testing'))

    def test_build_settings_raise_key_error(self):

        builder = Builder()
        env = dict()

        with self.assertRaises(UnknownEnvError):
            builder.settings(env, 'test')

    @patch('core.builder.os')
    def test_build_settings_success(self, fake_os):

        dict_environ = {
            'STATIC_PATH': '/testing',
            'STATIC_URL_PREFIX': '/testing_prefix'
        }

        fake_os.environ = dict_environ
        builder = Builder()

        env = {
            'DEBUG': True,
            'COMPRESS_RESPONSE': True,
            'XSRF': False,
            'STATIC_HASH_CACHE': False
        }

        settings = builder.settings(env)

        self.assertTrue(len(settings) > 0)
        self.assertEqual(settings['debug'], True)
        self.assertEqual(settings['compress_response'], True)
        self.assertEqual(settings['xsrf_cookies'], False)
        self.assertEqual(settings['static_hash_cache'], False)
        self.assertEqual(settings['static_path'], '/testing')
        self.assertEqual(settings['static_url_prefix'], '/testing_prefix')
