import requests

class RestCountriesAPI:
    BASE_URL = "https://restcountries.com/v3.1"

    def get_all_countries(self):
        url = f"{self.BASE_URL}/all"
        response = requests.get(url)
        return response
