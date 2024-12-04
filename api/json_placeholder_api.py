import requests

class JsonPlaceholderAPI:
    def __init__(self):
        self.url = 'https://jsonplaceholder.typicode.com/posts'

    def get(self):
        try:
            response = requests.get(self.url)
            return response
        except requests.RequestException as e:
            raise Exception(f"JSON Placeholder API request failed: {str(e)}")
