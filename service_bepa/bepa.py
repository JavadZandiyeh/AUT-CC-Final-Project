import os
import logging
import requests
from datetime import datetime
from time import sleep
from .db_handler import MySqlHandler

# Environmental Variables
## bepa config
INTERVAL_SECONDS    = os.getenv('INTERVAL_SECONDS')
COINNEWS_ENDPOINT   = os.getenv('COINNEWS_ENDPOINT')

# instantiate logger
logging.basicConfig()
logger = logging.getLogger(__name__)

# instantiate db_handler
db_handler = MySqlHandler(logger)

def fetch_coin_data():
    try:
        change_percentage_dict = {}
        coin_name_list = requests.get(f'{COINNEWS_ENDPOINT}/api/data/').json()
        for coin_name in coin_name_list:
            coin_price_dict = requests.get(f'{COINNEWS_ENDPOINT}/api/data/{coin_name}/').json()
            coin_last_price_dict = db_handler.fetch_last_coin_price(coin_name)

            current_price = coin_price_dict['value']
            last_price = coin_last_price_dict['price']

            # TODO: recheck the formula
            change = abs(current_price - last_price) / last_price

            # write new value of `coin_name` to database
            db_handler.insert_coin_price(coin_name, current_price)

            change_percentage_dict[coin_name] = change

    except:
        pass

# loop
while True:
    logger.info(f"Starting at {datetime.now()}")
    sleep(INTERVAL_SECONDS)
    logger.info(f"Ending {INTERVAL_SECONDS} seconds later at {datetime.now()}")