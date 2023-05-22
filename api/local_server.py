from wsgiref.simple_server import make_server
from config.app import app

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, app=app)
    server.serve_forever()
