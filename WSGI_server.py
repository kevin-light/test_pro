from wsgiref.simple_server import make_server
from WSGI_test01 import application
httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()