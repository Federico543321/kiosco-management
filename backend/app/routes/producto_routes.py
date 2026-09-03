from flask import Blueprint, jsonify, request

from backend.app.services.producto_service import (
    obtener_productos_por_negocio,
    crear_producto_service,
    obtener_producto_por_id,
    actualizar_producto_service,
    eliminar_producto_service
)

from backend.app.utils.auth import obtener_usuario_desde_token


producto_routes = Blueprint("producto_routes", __name__)


@producto_routes.route("/negocios/<int:id_negocio>/productos", methods=["GET"])
def listar_productos(id_negocio):

    id_usuario = obtener_usuario_desde_token()

    if id_usuario is None:
        return jsonify({
            "mensaje": "Token inválido o ausente"
        }), 401

    productos = obtener_productos_por_negocio(id_negocio)

    return jsonify(productos), 200

@producto_routes.route("/negocios/<int:id_negocio>/productos", methods=["POST"])
def crear_nuevo_producto(id_negocio):

    id_usuario = obtener_usuario_desde_token()

    if id_usuario is None:
        return jsonify({
            "mensaje": "Token inválido o ausente"
        }), 401

    datos = request.get_json(silent=True)

    if datos is None:
        return jsonify({
            "mensaje": "El cuerpo de la petición debe ser JSON"
        }), 400

    id_categoria = datos.get("id_categoria")
    nombre = datos.get("nombre")
    marca = datos.get("marca")
    presentacion_gramaje = datos.get("presentacion_gramaje")
    codigo_barras = datos.get("codigo_barras")
    precio_venta = datos.get("precio_venta")
    stock_minimo = datos.get("stock_minimo")

    if not id_categoria or not nombre or precio_venta is None or stock_minimo is None:
        return jsonify({
            "mensaje": "Faltan datos obligatorios"
        }), 400

    id_producto = crear_producto_service(
        id_negocio,
        id_categoria,
        nombre,
        marca,
        presentacion_gramaje,
        codigo_barras,
        precio_venta,
        stock_minimo
    )

    return jsonify({
        "mensaje": "Producto creado correctamente",
        "id_producto": id_producto
    }), 201

@producto_routes.route("/negocios/<int:id_negocio>/productos/<int:id_producto>", methods=["GET"])
def obtener_producto(id_negocio, id_producto):

    id_usuario = obtener_usuario_desde_token()

    if id_usuario is None:
        return jsonify({
            "mensaje": "Token inválido o ausente"
        }), 401

    producto = obtener_producto_por_id(id_producto, id_negocio)

    if producto is None:
        return jsonify({
            "mensaje": "Producto no encontrado"
        }), 404

    return jsonify(producto), 200


@producto_routes.route(
    "/negocios/<int:id_negocio>/productos/<int:id_producto>",
    methods=["PUT"]
)
def actualizar_producto_route(id_negocio, id_producto):

    id_usuario = obtener_usuario_desde_token()

    if id_usuario is None:
        return jsonify({
            "mensaje": "Token inválido o ausente"
        }), 401

    datos = request.get_json(silent=True)

    if datos is None:
        return jsonify({
            "mensaje": "El cuerpo de la petición debe ser JSON"
        }), 400

    id_categoria = datos.get("id_categoria")
    nombre = datos.get("nombre")
    marca = datos.get("marca")
    presentacion_gramaje = datos.get("presentacion_gramaje")
    codigo_barras = datos.get("codigo_barras")
    precio_venta = datos.get("precio_venta")
    stock_minimo = datos.get("stock_minimo")

    if not id_categoria or not nombre or precio_venta is None or stock_minimo is None:
        return jsonify({
            "mensaje": "Faltan datos obligatorios"
        }), 400

    filas_afectadas = actualizar_producto_service(
        id_producto,
        id_negocio,
        id_categoria,
        nombre,
        marca,
        presentacion_gramaje,
        codigo_barras,
        precio_venta,
        stock_minimo
    )

    if filas_afectadas == 0:
        return jsonify({
            "mensaje": "Producto no encontrado"
        }), 404

    return jsonify({
        "mensaje": "Producto actualizado correctamente"
    }), 200

@producto_routes.route(
    "/negocios/<int:id_negocio>/productos/<int:id_producto>",
    methods=["DELETE"]
)

def eliminar_producto_route(id_negocio, id_producto):

    id_usuario = obtener_usuario_desde_token()

    if id_usuario is None:
        return jsonify({
            "mensaje": "Token inválido o ausente"
        }), 401

    filas_afectadas = eliminar_producto_service(
        id_producto,
        id_negocio
    )

    if filas_afectadas == 0:
        return jsonify({
            "mensaje": "Producto no encontrado"
        }), 404

    return jsonify({
        "mensaje": "Producto eliminado correctamente"
    }), 200