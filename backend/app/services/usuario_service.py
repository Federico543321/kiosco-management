from backend.app.repositories.usuario_repository import (
    buscar_por_nombre_usuario,
    buscar_por_id_usuario,
    buscar_rol_usuario_negocio,
    crear_usuario as crear_usuario_repository
)

from backend.app.utils.security import generar_hash, verificar_password

def obtener_usuario_por_nombre_usuario(nombre_usuario):
    usuario = buscar_por_nombre_usuario(nombre_usuario)

    if usuario is None:
        return None

    if usuario["estado"] != "ACTIVO":
        return None

    return usuario
    
def obtener_usuario_por_id(id_usuario):
    return buscar_por_id_usuario(id_usuario)

def crear_usuario(nombre, nombre_usuario, password, email, telefono):
    usuario_existente = buscar_por_nombre_usuario(nombre_usuario)

    if usuario_existente is not None:
        return None

    if not nombre or not nombre_usuario or not password:
        return None

    password_hash = generar_hash(password)

    return crear_usuario_repository(
        nombre,
        nombre_usuario,
        password_hash,
        email,
        telefono,
        "ACTIVO"
    )

def autenticar_usuario(nombre_usuario, password):
    usuario = buscar_por_nombre_usuario(nombre_usuario)

    if usuario is None:
        return None

    if usuario["estado"] != "ACTIVO":
        return None

    if not verificar_password(password, usuario["password_hash"]):
        return None

    return usuario

def obtener_rol_usuario_negocio(id_usuario, id_negocio):
    resultado = buscar_rol_usuario_negocio(id_usuario, id_negocio)

    if resultado is None:
        return None

    return resultado["rol"]

def usuario_tiene_rol(id_usuario, id_negocio, rol_requerido):
    rol = obtener_rol_usuario_negocio(id_usuario, id_negocio)

    if rol is None:
        return False

    return rol == rol_requerido