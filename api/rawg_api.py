import requests

class RawgAPI:
    def __init__(self):
        self.url = 'https://api.rawg.io/api/games'
        self.params = {'key': 'PUTKEYHERE'}

    def get(self):
        try:
            response = requests.get(self.url, params=self.params)
            return response
        except requests.RequestException as e:
            raise Exception(f"RAWG API request failed: {str(e)}")
