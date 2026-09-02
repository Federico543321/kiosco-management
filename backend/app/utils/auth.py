from flask import request
from backend.app.utils.jwt import verificar_token


def obtener_usuario_desde_token():
    encabezado = request.headers.get("Authorization")

    if encabezado is None:
        return None

    partes = encabezado.split(" ")

    if len(partes) != 2:
        return None

    tipo, token = partes

    if tipo != "Bearer":
        return None

    payload = verificar_token(token)

    if payload is None:
        return None

    return payload["id_usuario"]