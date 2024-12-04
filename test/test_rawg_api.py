import unittest
from api.rest_countries_api import RestCountriesAPI

class TestRestCountriesAPI(unittest.TestCase):
    def setUp(self):
        self.api = RestCountriesAPI()

    def test_get(self):
        response = self.api.get()
        self.assertEqual(response.status_code, 200)
