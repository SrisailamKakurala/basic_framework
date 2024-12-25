from .request import Request

class Router:
    def __init__(self, app):
        self.app = app
        self.routes = {
            "/": self.index,
        }

    def handle_request(self, request, client_address, server):
        self.request = Request(request, client_address)
        path = self.request.path

        if path in self.routes:
            handler = self.routes[path]
            response = handler()
            self.request.send_response(200, {"Content-type": "text/html"})
            self.request.write(response)
        else:
            self.request.send_error(404, "Page Not Found")

    def index(self):
        return self.app.template_engine.render("index.html", message="Welcome to my basic framework!")
