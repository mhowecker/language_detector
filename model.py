import requests

class Model():
    def __init__(self):
        super().__init__()
    
    def detect_language(self, text: str) -> dict or None:
        try:
            r = requests.get('http://127.0.0.1:5000/lg?id=' + text)
        except:
            return None
        if r.status_code == 200:
            return r.text
        else:
            return None