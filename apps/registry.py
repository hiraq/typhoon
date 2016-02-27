from apps.hello.routes import routes as HelloApp
from apps.ping.routes import routes as PingApp

"""
You should register all of your apps here.
"""
apps = []
apps.extend(HelloApp)
apps.extend(PingApp)
