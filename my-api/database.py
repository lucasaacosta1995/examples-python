import mysql.connector
from mysql.connector import Error
from config import Config

def get_db_connection():
    try:
        conexion = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        return conexion
    except Error as e:
        print(f"Error de conexión a MySQL: {e}")
        return None  # Retorna None si hay un error
