import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../../')

import unittest
import logging

from tornado.log import app_log as logger
from mock import MagicMock, patch
from core.setting.session import Session, session_settings

class TestSession(unittest.TestCase):

    def test_session_init(self):

        dict_session = dict(
            SESSION_ENGINE = 'redis'
        )

        session = Session(dict_session)
        self.assertEqual(session.config, dict_session)

    def test_session_empty_dict(self):

        dict_session = dict(
            SESSION_ENGINE = 'test'
        )

        session = Session(dict_session)
        sess_config = session.get_used_config()
        self.assertTrue(len(sess_config) < 1)

    def test_session_redis_success_all(self):

        dict_session = dict(
            SESSION_ENGINE = 'REDIS',
            SESSION_REDIS_HOST = "localhost",
            SESSION_REDIS_PORT = 6379,
            SESSION_REDIS_DB = 0,
            SESSION_REDIS_PASSWORD = 'testing',
            SESSION_REDIS_MAX_CONNECTIONS = 2048
        )

        session = Session(dict_session)
        sess_config = session.get_used_config()

        self.assertTrue(len(sess_config) >= 1)
        self.assertEqual(sess_config['driver'], 'redis')
        self.assertEqual(sess_config['driver_settings']['host'], 'localhost')
        self.assertEqual(sess_config['driver_settings']['port'], 6379)
        self.assertEqual(sess_config['driver_settings']['db'], 0)
        self.assertEqual(sess_config['driver_settings']['password'], 'testing')
        self.assertEqual(sess_config['driver_settings']['max_connections'], 2048)

    def test_session_redis_success_default(self):

        dict_session = dict(
            SESSION_ENGINE = 'REDIS',
            SESSION_REDIS_HOST = "localhost",
            SESSION_REDIS_PORT = 6379,
            SESSION_REDIS_DB = 0
        )

        session = Session(dict_session)
        sess_config = session.get_used_config()

        self.assertTrue(len(sess_config) >= 1)
        self.assertEqual(sess_config['driver'], 'redis')
        self.assertEqual(sess_config['driver_settings']['host'], 'localhost')
        self.assertEqual(sess_config['driver_settings']['port'], 6379)
        self.assertEqual(sess_config['driver_settings']['db'], 0)
        self.assertEqual(sess_config['driver_settings']['password'], None)
        self.assertEqual(sess_config['driver_settings']['max_connections'], 1024)

    def test_session_memcache_success(self):

        dict_session = dict(
            SESSION_ENGINE = 'MEMCACHE',
            SESSION_MEMCACHE_HOST = "localhost",
            SESSION_MEMCACHE_PORT = 11211,
        )

        session = Session(dict_session)
        sess_config = session.get_used_config()

        self.assertTrue(len(sess_config) >= 1)
        self.assertEqual(sess_config['driver'], 'memcached')
        self.assertEqual(sess_config['driver_settings']['host'], 'localhost')
        self.assertEqual(sess_config['driver_settings']['port'], 11211)

    @patch('core.setting.session.os')
    def test_session_function(self,fake_os):

        dict_session = dict(
            SESSION_ENGINE = 'MEMCACHE',
            SESSION_MEMCACHE_HOST = "localhost",
            SESSION_MEMCACHE_PORT = 11211,
        )

        fake_os.environ = dict_session
        sess_config = session_settings()
        self.assertTrue(len(sess_config) >= 1)
        self.assertEqual(sess_config['driver'], 'memcached')
        self.assertEqual(sess_config['driver_settings']['host'], 'localhost')
        self.assertEqual(sess_config['driver_settings']['port'], 11211)
