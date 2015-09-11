import unittest
import json
import urllib

__author__ = 'Lorenzo'


def get_curling(url, params=dict()):
    import pycurl
    import urllib
    from StringIO import StringIO

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    if len(params.keys()) != 0:
        c.setopt(c.URL, url + '?' + urllib.urlencode(params))
        print url + '?' + urllib.urlencode(params)
    print url
    # For older PycURL versions:
    #c.setopt(c.WRITEFUNCTION, buffer.write)
    c.perform()
    c.close()

    body = buffer.getvalue()
    # Body is a string in some encoding.
    # In Python 2, we can print it without knowing what the encoding is.
    return body


def test_integrity(res):
    try:
        res = json.loads(res)
        return res
    except Exception:
        print "the endpoint response was in the wrong format or status 400 or 500"
        assert False


def test_endpoints(env):
    envs = {
        'local': 'http://localhost:8080/',
        'remote': 'http://mild-ql.appspot.com/'
    }
    base_url = envs[env]
    tests = ['', 'component', 'component/c']
    responses = [get_curling(base_url + t) for t in tests]

    for i, r in enumerate(responses):
        print i, r
        test_integrity(r)


if __name__ == '__main__':
    env = 'local'
    test_endpoints(env)