import hashlib
import os

class Security:
    def __init__(self):
        self.csrf_tokens = {}

    def generate_csrf_token(self):
        return hashlib.sha256(os.urandom(64)).hexdigest()

    def check_csrf_token(self, token):
        if token in self.csrf_tokens:
            return True
        return False
