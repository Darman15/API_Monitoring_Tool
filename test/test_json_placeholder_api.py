import unittest
from api.json_placeholder_api import JsonPlaceholderAPI

class TestJsonPlaceholderAPI(unittest.TestCase):
    def setUp(self):
        self.api = JsonPlaceholderAPI()

    def test_get(self):
        response = self.api.get()
        self.assertEqual(response.status_code, 200)
