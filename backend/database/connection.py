
import mysql.connector
from config import Config
import pymysql

def get_db_connection():
    try:
        # Using mysql-connector-python (primary)
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DATABASE
        )
        return connection
    except mysql.connector.Error as err:
        print(f"MySQL Connector Error: {err}")
        try:
            # Fallback to PyMySQL
            connection = pymysql.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DATABASE,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return connection
        except pymysql.Error as err:
            print(f"PyMySQL Error: {err}")
            return None