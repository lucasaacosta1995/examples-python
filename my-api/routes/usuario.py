from flask import Blueprint, jsonify, request
from models.usuario import Usuario

usuario_bp = Blueprint("usuario_bp", __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.obtener_todos()
    if "error" in usuarios:
        return jsonify(usuarios), 500
    return jsonify(usuarios)

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.obtener_por_id(id)
    if usuario is None:
        return jsonify({"error": "Error de conexión a la base de datos"}), 500
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario)

@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.json
    if not datos.get("nombre") or not datos.get("email"):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    nuevo_usuario = Usuario(nombre=datos["nombre"], email=datos["email"])
    resultado = nuevo_usuario.guardar()
    if "error" in resultado:
        return jsonify(resultado), 500
    return jsonify(resultado), 201

@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    datos = request.json
    if not datos.get("nombre") or not datos.get("email"):
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    usuario = Usuario(id=id, nombre=datos["nombre"], email=datos["email"])
    resultado = usuario.actualizar()
    if "error" in resultado:
        return jsonify(resultado), 500
    return jsonify(resultado)

@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    resultado = Usuario.eliminar(id)
    if "error" in resultado:
        return jsonify(resultado), 500
    return jsonify(resultado)
