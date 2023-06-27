import os
import pymysql
import logging
from typing import Dict, Union, Tuple


class MySqlHandler:

    def __init__(self, logger: logging.Logger) -> None:
        """initiate MySqlHandler object

        Args:
            logger (logging.Logger): logger object
        """
        self.logger = logger
        ## MySQL credentials
        self.host           = os.getenv('MYSQL_HOST')
        self.port           = int(os.getenv('MYSQL_PORT'))
        self.user           = 'root'
        self.database       = os.getenv('MYSQL_DATABASE')
        self.password       = os.getenv('MYSQL_ROOT_PASSWORD')
        self.cursor_class   = pymysql.cursors.DictCursor
        self.coin_set       = set()

        self.conn = self.init_connection()


    def init_connection(self) -> pymysql.Connection:
        try:
            connection = pymysql.connect(host=self.host,
                                        port=self.port,
                                        user=self.user,
                                        passwd=self.password,
                                        db=self.database,
                                        cursorclass=self.cursor_class)
            self.logger.info('[+] Local Connection Successful')
        except Exception as e:
            self.logger.exception(f'[+] Local Connection Failed: {e}', exc_info=True)
            connection = None

        return connection
    
    def init_coin_name(self, coin_list):
        sql = """
            INSERT INTO Coin (coin_name) VALUES (\"{coin_name}\")
        """
        with self.conn.cursor() as cursor:
            cursor.execute('select * from Coin')
            self.coin_set = set(record['coin_name'] for record in cursor.fetchall())
            self.conn.commit()

            for coin_name in list(set(coin_list) - self.coin_set):
                try:
                    cursor.execute(sql.format(coin_name=coin_name))
                    self.coin_set.add(coin_name)
        
                    self.conn.commit()
                except pymysql.err.IntegrityError:
                    self.logger.info(f'`{coin_name}` already exist in `Coin` table')

                except Exception as e:
                    self.logger.error(f'error in `init_coin_name`: {e}', exc_info=True)
                
    
    def insert_coin_price(self, coin_name: str, price: float):
        sql = """
            INSERT INTO Prices (coin_name, price) VALUES ("{coin_name}", {price})
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql.format(coin_name=coin_name, price=price))

        self.conn.commit()

    def fetch_last_coin_price(self, coin_name: str):
        sql = """
            SELECT * FROM Prices WHERE coin_name="{coin_name}" ORDER BY time_stamp DESC
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql.format(coin_name=coin_name))

        self.conn.commit()

        return cursor.fetchone()
    
    def triggered_subscription(self, coin_name: str, change: float) -> Union[Tuple[Dict], None]:
        sql = """
            SELECT * FROM AlertSubscriptions WHERE difference_percentage <= {change_percentage}
        """
        change_percentage = int(change * 100)
        self.logger.info(f'{sql.format(change_percentage=change_percentage)=}')

        with self.conn.cursor() as cursor:
            cursor.execute(sql.format(change_percentage=change_percentage))

        self.conn.commit()

        return cursor.fetchall()

