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