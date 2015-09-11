import sys
sys.path.insert(0, 'lib')
import json

import lib.falcon as falcon

from google.appengine.ext.webapp.util import run_wsgi_app

__author__ = 'lorenzo'


class Entrypoint(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.body = json.dumps([{"element": "/component"}, {"collection": "/component/c"}])


class ComponentResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.body = json.dumps({"id": "123"})


class ComponentCollection(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.body = json.dumps([{"id": "123"}, {"id": "124"}, {"id": "125"}])


# Resources are represented by long-lived class instances
component = ComponentResource()
collection = ComponentCollection()
entrypoint = Entrypoint()

# falcon.API instances are callable WSGI apps
api = falcon.API()

# things will handle all requests to the '/things' URL path
api.add_route('/component/c', collection)
api.add_route('/component', component)
api.add_route('/', entrypoint)


def main():
    run_wsgi_app(api)

if __name__ == '__main__':
    main()

