import os

class StaticFileHandler:
    def __init__(self):
        self.static_dir = os.path.join(os.path.dirname(__file__), "../static")

    def handle_static(self, file_name):
        file_path = os.path.join(self.static_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                return file.read()
        else:
            return None
