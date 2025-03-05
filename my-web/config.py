import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Cambia por tu host
        user="root",       # Cambia por tu usuario de MySQL
        password="",  # Cambia por tu contraseña de MySQL
        database="flask_db"  # Cambia por el nombre de tu base de datos
    )
