import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mi_base"
    )

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    return jsonify(usuarios)

@app.route('/api/usuarios', methods=['POST'])
def create_usuario():
    datos = request.json
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (datos["nombre"],))
    conexion.commit()
    conexion.close()
    return jsonify({"mensaje": "Usuario creado"}), 201

if __name__ == '__main__':
    app.run(debug=True)
