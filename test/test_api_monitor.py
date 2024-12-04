import unittest
from api_monitor import APIMonitor

class TestAPIMonitor(unittest.TestCase):
    def setUp(self):
        self.api_monitor = APIMonitor()

    def test_monitor_apis(self):
        # This test ensures the monitor_apis method runs without errors
        try:
            self.api_monitor.monitor_apis()
        except Exception as e:
            self.fail(f"monitor_apis raised an exception: {str(e)}")
