from backend.app.repositories.producto_repository import (
    listar_productos_por_negocio,
    crear_producto,
    buscar_producto_por_id,
    actualizar_producto,
    eliminar_producto
)

def obtener_productos_por_negocio(id_negocio):
    return listar_productos_por_negocio(id_negocio)

def obtener_producto_por_id(id_producto, id_negocio):
    return buscar_producto_por_id(id_producto, id_negocio)

def actualizar_producto_service(
    id_producto,
    id_negocio,
    id_categoria,
    nombre,
    marca,
    presentacion_gramaje,
    codigo_barras,
    precio_venta,
    stock_minimo
):
    return actualizar_producto(
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
    
def eliminar_producto_service(id_producto, id_negocio):

    return eliminar_producto(
        id_producto,
        id_negocio
    )

def crear_producto_service(
    id_negocio,
    id_categoria,
    nombre,
    marca,
    presentacion_gramaje,
    codigo_barras,
    precio_venta,
    stock_minimo
):
    return crear_producto(
        id_negocio,
        id_categoria,
        nombre,
        marca,
        presentacion_gramaje,
        codigo_barras,
        precio_venta,
        stock_minimo
    )