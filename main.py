import sys
sys.path.insert(0, 'lib')

import json
import falcon as falcon
from google.appengine.ext.webapp.util import run_wsgi_app

__author__ = 'lorenzo'

from config import _SERVICE, _DEBUG


class Entrypoint(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.body = json.dumps([
            {"example": _SERVICE + "/component/123"},
            {"collection": _SERVICE + "/component/c"},
            {"subsystem": _SERVICE + "/subsystem/c"}
        ])


class ComponentResource(object):
    def on_get(self, req, resp, **params):
        """Handles GET requests"""
        resp.content_type = "application/json"

        from unittesting.mock_endpoints import components

        component = [c
                     for c in components
                     if c['uuid'] == params['uuid']]
        if component:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(component[0], indent=2)
            return

        resp.status = falcon.HTTP_404


class ComponentCollection(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        from unittesting.mock_endpoints import components

        components = [{'name': c['name'],
                       'uuid': c['uuid'],
                       'type_(not implemented)': _SERVICE + "/subsystem/" + c['type'][c['type'].rfind('/') + 1:]}
             for c in components]

        resp.body = json.dumps(components, indent=2)


class SubsystemResource(object):
    def on_get(self, req, resp, **params):
        """Handles GET requests"""
        resp.content_type = "application/json"

        from unittesting.mock_endpoints import subsystems

        results = [s
                     for s in subsystems
                     if s['name'][s['name'].rfind('/') + 1:] == params['slug']]
        if component:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(results[0], indent=2)
            return

        resp.status = falcon.HTTP_404


class SubsystemCollection(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        from unittesting.mock_endpoints import subsystems

        results = [s
                   for s in subsystems]

        resp.body = json.dumps(results, indent=2)

# Resources are represented by long-lived class instances
component = ComponentResource()
collection = ComponentCollection()
subsystem_res = SubsystemResource()
subsystem_col = SubsystemCollection()
entrypoint = Entrypoint()

# falcon.API instances are callable WSGI apps
api = falcon.API()

# things will handle all requests to the '/things' URL path
api.add_route('/component/c', collection)
api.add_route('/component/{uuid}', component)
api.add_route('/subsystem/c', subsystem_col)
api.add_route('/subsystem/{slug}', subsystem_res)
api.add_route('/', entrypoint)


def main():
    run_wsgi_app(api)

if __name__ == '__main__':
    main()

