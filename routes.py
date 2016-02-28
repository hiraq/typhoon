from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from apps.registry import apps

class RoutesBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Command Line Tools - Routes'

    @expose(hide=True)
    def default(self):
        print 'Use: "python routes.py list"'

class RouteListController(CementBaseController):
    class Meta:
        label = 'list'
        stacked_on = 'base'

    @expose(help='List of registered routes', aliases=['list'])
    def list_routes(self):
        
        def build_routes(name, route):
            return [name,route[0], route[1].__name__, route[2]]

        headers = ['APPLICATION NAME','PATH', 'HANDLER', 'METHOD']
        data = []
        for app in apps.get_apps():
            routes = app.routes()
            for route in routes:
                data.append(build_routes(app.name(), route))

        self.app.render(data, headers=headers)

class RouteApp(CementApp):
    class Meta:
        label = 'routes'
        base_controller = 'base'
        extensions = ['tabulate']
        output_handler = 'tabulate'
        handlers = [RoutesBaseController, RouteListController]

with RouteApp() as cli:
    cli.run()
