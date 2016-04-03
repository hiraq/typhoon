from apps.hello.routes import app as HelloApp
from apps.ping.routes import app as PingApp
from core.registry import Registry

"""
You should register all of your apps here.
"""
apps = Registry()
apps.register(HelloApp)
apps.register(PingApp)
