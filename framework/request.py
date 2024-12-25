import socket

class Request:
    def __init__(self, request, client_address):
        self.raw_request = request
        self.client_address = client_address
        self.path = self.parse_path()
        self.headers = {}

    def parse_path(self):
        data = self.raw_request.recv(1024)
        path = data.split(b" ")[1].decode("utf-8")
        return path

    def send_response(self, code, headers=None):
        if headers is None:
            headers = {}
        self.headers = headers
        self.raw_request.send(f"HTTP/1.1 {code} OK\r\n".encode())
        for header, value in self.headers.items():
            self.raw_request.send(f"{header}: {value}\r\n".encode())
        self.raw_request.send("\r\n".encode())  # End of headers

    def send_error(self, code, message):
        self.send_response(code)
        self.send_header("Content-type", "text/html")
        self.raw_request.send(f"<h1>{message}</h1>".encode())

    def send_header(self, header, value):
        self.raw_request.send(f"{header}: {value}\r\n".encode())

    def write(self, data):
        self.raw_request.send(data.encode())
