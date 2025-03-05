import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mi_base"
)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM usuarios")

for fila in cursor.fetchall():
    print(fila)

conexion.close()
