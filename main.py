__author__ = 'lorenzo'


import sys
sys.path.insert(0, 'lib')

import lib.falcon as falcon
from wsgiref import simple_server


class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        parsed = parse_graphql()
        resp.body = str(parsed)


from lib.graphql.parser import GraphQLParser


def parse_graphql():
    parser = GraphQLParser()
    ast = parser.parse("""
    {
      user(id: 4) {
        id
        name
        profilePic
        avatar: profilePic(width: 30, height: 30)
      }
    }
    """)
    print(ast)
    return ast


# Resources are represented by long-lived class instances
things = ThingsResource()

# falcon.API instances are callable WSGI apps
api = falcon.API()

# things will handle all requests to the '/things' URL path
api.add_route('/things', things)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 5000, api)
    httpd.serve_forever()