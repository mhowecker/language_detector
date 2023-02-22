import view
import model
import json
from PyQt6.QtWidgets import QApplication
import sys


class Client():

    def __init__(self):
        super().__init__()
        
        self.view = view.View(self)
        self.model = model.Model()

    def detect_language(self, text: str) -> dict or None:
        response = self.model.detect_language(text)
        response = response = dict(json.loads(response))
        return response

    def exit_view(self):
        self.view.exit()

    def reset_view(self):
        self.view.reset()

if __name__ == '__main__':
    app = QApplication([])
    c = Client()
    c.view.show()
    sys.exit(app.exec())