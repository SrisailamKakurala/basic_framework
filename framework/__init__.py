from .routing import Router
from .request import Request
from .security import Security
from .templates import TemplateEngine
from .static import StaticFileHandler

class Framework:
    def __init__(self):
        self.router = Router(self)
        self.template_engine = TemplateEngine()
        self.static_handler = StaticFileHandler()
        self.security = Security()

    def run(self, host="127.0.0.1", port=8080):
        from http.server import HTTPServer
        server = HTTPServer((host, port), self.router.handle_request)
        print(f"Server running at http://{host}:{port}")
        server.serve_forever()
