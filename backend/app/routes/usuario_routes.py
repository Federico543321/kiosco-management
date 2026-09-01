from flask import Blueprint, jsonify, request
from backend.app.services.usuario_service import (
    obtener_usuario_por_nombre_usuario,
    crear_usuario as crear_usuario_service
)
usuario_routes = Blueprint("usuario_routes", __name__)


@usuario_routes.route("/usuarios/<nombre_usuario>", methods=["GET"])
def obtener_usuario(nombre_usuario):
    usuario = obtener_usuario_por_nombre_usuario(nombre_usuario)

    if usuario is None:
        return jsonify({
            "mensaje": "Usuario no encontrado"
        }), 404

    return jsonify(usuario), 200

@usuario_routes.route("/usuarios", methods=["POST"])
def crear_usuario():
    datos = request.get_json(silent = True)

    
    if datos is None:
        return jsonify({
        "mensaje": "El cuerpo de la petición debe ser JSON"
        }), 400

    nombre = datos.get("nombre")
    nombre_usuario = datos.get("nombre_usuario")
    password = datos.get("password")
    email = datos.get("email")
    telefono = datos.get("telefono")

    if not nombre or not nombre_usuario or not password:
        return jsonify({
            "mensaje": "Faltan datos obligatorios"
        }), 400

    id_usuario = crear_usuario_service(
        nombre,
        nombre_usuario,
        password,
        email,
        telefono
    )

    if id_usuario is None:
        return jsonify({
            "mensaje": "El nombre de usuario ya existe o los datos son inválidos"
        }), 400

    return jsonify({
        "mensaje": "Usuario creado correctamente",
        "id_usuario": id_usuario
    }), 201