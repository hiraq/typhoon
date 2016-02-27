from apps.hello.routes import app as HelloApp
from apps.ping.routes import app as PingApp

"""
You should register all of your apps here.
"""
apps = []
apps.extend(HelloApp.routes())
apps.extend(PingApp.routes())
