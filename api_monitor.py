import logging
import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from api.rawg_api import RawgAPI
from api.rest_countries_api import RestCountriesAPI
from api.json_placeholder_api import JsonPlaceholderAPI

class APIMonitor:
    def __init__(self):
        self.scheduler = BlockingScheduler()
        self.setup_logging()

    def setup_logging(self):
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        log_filename = f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"
        logging.basicConfig(filename=log_filename, 
                            level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_error(self, message):
        logging.error(message)

    def monitor_apis(self):
        try:
            apis = [
                RawgAPI(),
                RestCountriesAPI(),
                JsonPlaceholderAPI()
            ]

            for api in apis:
                try:
                    response = api.get()
                    if response.status_code == 200:
                        logging.info(f"API {api.__class__.__name__}: Success with status code {response.status_code}")
                    else:
                        logging.warning(f"API {api.__class__.__name__}: Failure with status code {response.status_code}")
                except Exception as e:
                    self.log_error(f"API {api.__class__.__name__}: Exception occurred - {str(e)}")
        except Exception as e:
            self.log_error(f"Error occurred in monitor_apis: {str(e)}")

    def start_monitoring(self):
        # Initial run at startup
        self.monitor_apis()
        
        # Schedule to run every 15 minutes
        self.scheduler.add_job(self.monitor_apis, 'interval', minutes=15)
        self.scheduler.start()
