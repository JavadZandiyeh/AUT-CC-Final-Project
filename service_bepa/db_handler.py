import os
import pymysql
import logging


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
        self.user           = os.getenv('MYSQL_USER')
        self.database       = os.getenv('MYSQL_DATABASE')
        self.password       = os.getenv('MYSQL_ROOT_PASSWORD')
        self.cursor_class   = pymysql.cursors.DictCursor

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
    
    def insert_coin_price(self, coin_name: str, price: float):
        sql = """
            INSERT INTO Price (coin_name, price) values ({coin_name}, {price})
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql.format(coin_name, price))

        self.conn.commit()

    def fetch_last_coin_price(self, coin_name: str):
        sql = """
            SELECT * FROM Price WHERE coin_name={coin_name} ORDER BY time_stamp DESC
        """
        with self.conn.cursor() as cursor:
            cursor.execute(sql.format(coin_name))

        self.conn.commit()

        return cursor.fetchone()
