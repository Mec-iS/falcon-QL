import os
__author__ = 'Lorenzo'

_ENV = {'offline': {'_SERVICE': 'http://localhost:7000',
                    '_DEBUG': True},
        'online': {'_SERVICE': 'http://mild-ql.appspot.com',
                   '_DEBUG': True}}


def set_env_variables():
    if not 'SERVER_SOFTWARE' in os.environ or os.environ['SERVER_SOFTWARE'].startswith('Development'):
        _SERVICE, _DEBUG = _ENV['offline']['_SERVICE'], _ENV['offline']['_DEBUG']

        from google.appengine.tools.devappserver2.python import sandbox
        sandbox._WHITE_LIST_C_MODULES += ['_ssl', '_socket']

    else:
        _SERVICE, _DEBUG = _ENV['online']['_SERVICE'], _ENV['online']['_DEBUG']


    return _SERVICE, _DEBUG

_SERVICE, _DEBUG = set_env_variables()
