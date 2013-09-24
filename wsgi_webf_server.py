import sys
from app import app as application

# sys.path.insert(0, '/home/engineroom/webapps/shopify_whooks')
# from shopify_whooks import app as application

class WebFactionMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = '/shopify/webhooks'
        return self.app(environ, start_response)

application.wsgi_app = WebFactionMiddleware(application.wsgi_app)
