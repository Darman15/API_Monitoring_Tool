import unittest
from api.rest_countries import RestCountriesAPI

class TestRestCountriesAPI(unittest.TestCase):
    def setUp(self):
        self.api = RestCountriesAPI()

    def test_get_all_countries(self):
        response = self.api.get_all_countries()
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
