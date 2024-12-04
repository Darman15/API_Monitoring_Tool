import requests

class RestCountriesAPI:
    def __init__(self):
        self.url = 'https://restcountries.com/v3.1/all'

    def get(self):
        try:
            response = requests.get(self.url)
            return response
        except requests.RequestException as e:
            raise Exception(f"REST Countries API request failed: {str(e)}")
