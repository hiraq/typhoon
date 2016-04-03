from apps.hello.routes import app as HelloApp
from apps.ping.routes import app as PingApp
from core.registry import Registry
from core.exceptions.application import ContainerError

try:

    """
    You should register all of your apps here.
    """
    apps = Registry()
    apps.register(HelloApp)
    apps.register(PingApp)

except ContainerError, e:

    """
    I cannot use logging here.  If i use default logging here,
    it will reset all tornado's logging configurations, so i just
    use simple print statement.
    """
    print e.message 