import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')

import unittest
from mock import MagicMock
from core.session import Session

class FakeYamlObject(object):
    """Fake Yaml Object

    This object used as mocking yaml and add 'set'
    method to add key, value
    """
    def __init__(self):
        self.props = {}

    def set(self, key, value):
        self.props[key] = value

    def get(self, key):
        self.props[key]

    def as_dict(self):
        return self.props

class TestSession(unittest.TestCase):

    def setUp(self):
        self.redis = FakeYamlObject()
        self.redis.set('SESSION_ENGINE', 'REDIS')
        self.redis.set('SESSION_DRIVERS', dict(
            REDIS = dict(
                HOST = 'localhost',
                PORT = 7700,
                DB = 1
            )
        ))

        self.memcache = FakeYamlObject()
        self.memcache.set('SESSION_ENGINE', 'MEMCACHE')
        self.memcache.set('SESSION_DRIVERS', dict(
            MEMCACHE = dict(
                HOST = 'localhost',
                PORT = 11211
            )
        ))

    def test_empty_dict(self):
        yaml = FakeYamlObject()
        yaml.set('SESSION_ENGINE', 'test')
        yaml.set('SESSION_DRIVERS', dict())

        session = Session(yaml)
        session_settings = session.get_used_config()
        self.assertEqual(0, len(session_settings.keys()))

    def test_redis_dict(self):
        session = Session(self.redis.as_dict())
        session_settings = session.get_used_config()
        self.assertEqual('redis',session_settings['driver'])
        self.assertEqual(7700,session_settings['driver_settings']['port'])
        self.assertEqual(1,session_settings['driver_settings']['db'])

    def test_memcache_dict(self):
        session = Session(self.memcache.as_dict())
        session_settings = session.get_used_config()
        self.assertEqual('memcached',session_settings['driver'])
        self.assertEqual(11211,session_settings['driver_settings']['port'])
