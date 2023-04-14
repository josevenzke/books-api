from wsgiref.simple_server import make_server
from api import app


server = make_server('localhost', 8000, app=app)
server.serve_forever()