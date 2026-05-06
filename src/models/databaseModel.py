import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            return connection

        except Exception as e:
            print("Error al conectar a la base de datos:", e)
            return None