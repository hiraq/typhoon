import os
import psycopg2
import momoko
from tornado.ioloop import IOLoop

def settings():
    ioloop = IOLoop.instance()
    return momoko.Pool(
        dsn=os.environ.get('MOMOKO_DSN'),
        size=os.environ.get('MOMOKO_SIZE'),
        ioloop=ioloop
    )
