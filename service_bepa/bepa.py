import os
import logging
import requests
from time import sleep
from typing import Dict
from datetime import datetime
from db_handler import MySqlHandler

# Environmental Variables
## bepa config
INTERVAL_SECONDS    = int(os.getenv('INTERVAL_SECONDS'))
COINNEWS_ENDPOINT   = os.getenv('COINNEWS_ENDPOINT')

# instantiate logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# instantiate db_handler
db_handler = MySqlHandler(logger)

def send_email(record: Dict):
    logger.info(f"send email to {record['email']} for {record['coin_name']}")
    requests.post(
        "https://api.mailgun.net/v3/sandbox994f65065c4c40b885b65de02bf4b35b.mailgun.org/messages",
        auth=("api", "9a71d6d5cb1dfa0da9b3135cd413ee96-e5475b88-b37ed9c3"),
        data={"from": "Bepa <mailgun@sandbox994f65065c4c40b885b65de02bf4b35b.mailgun.org>",
              "to": f"<{record['email']}>",
              "subject": f"[ALERT] Subscription Triggered for ({record['coin_name']})",
              "text": f"""
Hi,
Your subscription for {record['coin_name']} triggered:
your submitted difference percentage = {record['difference_percentage']}
current difference percentage = {record['change_percentage']}
                """.strip()})

def fetch_coin_data():
    try:
        change_percentage_dict = {}
        coin_name_list = requests.get(f'{COINNEWS_ENDPOINT}/api/data/').json()

        # init coin names
        db_handler.init_coin_name(coin_name_list)
        
        for coin_name in coin_name_list:
            try:
                coin_price_dict = requests.get(f'{COINNEWS_ENDPOINT}/api/data/{coin_name}/').json()
                coin_last_price_dict = db_handler.fetch_last_coin_price(coin_name)
                
                current_price = coin_price_dict['value']

                if coin_last_price_dict is not None:

                    last_price = coin_last_price_dict['price']

                    logger.info(f'{coin_name}')
                    logger.info(f'{current_price=}, {last_price=}')

                    if last_price == 0.0:
                        last_price += 0.1
                        
                    # TODO: recheck the formula
                    change = abs(current_price - last_price) / abs(last_price)
                    logger.info(f'{change=}')
                    change_percentage_dict[coin_name] = change

                # write new value of `coin_name` to database
                db_handler.insert_coin_price(coin_name, current_price)

                triggered_records = db_handler.triggered_subscription(coin_name, change)
                for triggered_record in triggered_records:
                    triggered_record['change_percentage'] = change
                    send_email(triggered_record)

            except Exception as e:
                logger.error(f'fetch {coin_name} price failed: {e}', exc_info=True)

    except Exception as e:
        logger.error(f'fetch coin prices failed, {e}', exc_info=True)

# loop
while True:
    logger.info(f"Starting at {datetime.now()}")
    fetch_coin_data()
    sleep(INTERVAL_SECONDS)
    logger.info(f"Ending {INTERVAL_SECONDS} seconds later at {datetime.now()}")