#def application(environ, start_response):
#	start_response('200 OK', [('Content-Type', 'text/html')])
#	return [b"<h1 style='color:blue'>Hello World2</h1>"]

#import Rest_Api/Config/wsgi.py

import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'Config/wsgi.py')
application = wsgi.application

