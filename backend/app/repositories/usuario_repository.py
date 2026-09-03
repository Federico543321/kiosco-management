from backend.app.database import obtener_conexion

def buscar_por_nombre_usuario(nombre_usuario):
    conexion = obtener_conexion()

    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM usuario
        WHERE nombre_usuario = %s
    """

    cursor.execute(sql, (nombre_usuario,))

    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    return usuario

def buscar_por_id_usuario(id_usuario):
    conexion = obtener_conexion()

    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM usuario
        WHERE id_usuario = %s
    """

    cursor.execute(sql, (id_usuario,))

    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    return usuario

def buscar_rol_usuario_negocio(id_usuario, id_negocio):
    conexion = obtener_conexion()

    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT rol
        FROM usuario_negocio
        WHERE id_usuario = %s
          AND id_negocio = %s
          AND estado = 'ACTIVO'
    """

    cursor.execute(sql, (id_usuario, id_negocio))

    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado

def crear_usuario(nombre, nombre_usuario, password_hash, email, telefono, estado):
    conexion = obtener_conexion()

    cursor = conexion.cursor()

    sql = """
        INSERT INTO usuario (
            nombre,
            nombre_usuario,
            password_hash,
            email,
            telefono,
            estado
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        nombre,
        nombre_usuario,
        password_hash,
        email,
        telefono,
        estado
    )

    cursor.execute(sql, valores)

    conexion.commit()

    id_usuario = cursor.lastrowid

    cursor.close()
    conexion.close()

    return id_usuario
