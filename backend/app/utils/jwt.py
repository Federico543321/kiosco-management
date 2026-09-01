import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "clave-secreta-desarrollo-kiosco-2026"

def generar_token(id_usuario):
    payload = {
        "id_usuario": id_usuario,
        "exp": datetime.now(timezone.utc) + timedelta(hours=2)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token

def verificar_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None