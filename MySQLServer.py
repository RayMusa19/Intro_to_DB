import mysql.connector
from mysql.connector import errorcode

def database_creation():
    try:
        cnx = mysql.connector.connect(
            user = root
            password = Daudavictoria1@
            host = 127.0.0.1
            port = 3306
        )
        cursor = cnx.cursor()

        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")
            exit(1)

        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
