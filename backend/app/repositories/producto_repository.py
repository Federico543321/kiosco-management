from backend.app.database import obtener_conexion


def listar_productos_por_negocio(id_negocio):
    conexion = obtener_conexion()

    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM producto
        WHERE id_negocio = %s
          AND estado = 'ACTIVO'
    """

    cursor.execute(sql, (id_negocio,))

    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return productos

def buscar_producto_por_id(id_producto, id_negocio):
    conexion = obtener_conexion()

    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM producto
        WHERE id_producto = %s
          AND id_negocio = %s
    """

    cursor.execute(sql, (id_producto, id_negocio))

    producto = cursor.fetchone()

    cursor.close()
    conexion.close()

    return producto

def actualizar_producto(
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
    conexion = obtener_conexion()

    cursor = conexion.cursor()

    sql = """
        UPDATE producto
        SET
            id_categoria = %s,
            nombre = %s,
            marca = %s,
            presentacion_gramaje = %s,
            codigo_barras = %s,
            precio_venta = %s,
            stock_minimo = %s
        WHERE id_producto = %s
          AND id_negocio = %s
    """

    valores = (
        id_categoria,
        nombre,
        marca,
        presentacion_gramaje,
        codigo_barras,
        precio_venta,
        stock_minimo,
        id_producto,
        id_negocio
    )

    cursor.execute(sql, valores)

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas
    
def eliminar_producto(id_producto, id_negocio):
    conexion = obtener_conexion()

    cursor = conexion.cursor()

    sql = """
        UPDATE producto
        SET estado = 'INACTIVO'
        WHERE id_producto = %s
          AND id_negocio = %s
    """

    cursor.execute(sql, (id_producto, id_negocio))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas

def crear_producto(
    id_negocio,
    id_categoria,
    nombre,
    marca,
    presentacion_gramaje,
    codigo_barras,
    precio_venta,
    stock_minimo
):
    conexion = obtener_conexion()

    cursor = conexion.cursor()

    sql = """
        INSERT INTO producto (
            id_negocio,
            id_categoria,
            nombre,
            marca,
            presentacion_gramaje,
            codigo_barras,
            precio_venta,
            stock_minimo,
            estado
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        id_negocio,
        id_categoria,
        nombre,
        marca,
        presentacion_gramaje,
        codigo_barras,
        precio_venta,
        stock_minimo,
        "ACTIVO"
    )

    cursor.execute(sql, valores)

    conexion.commit()

    id_producto = cursor.lastrowid

    cursor.close()
    conexion.close()

    return id_producto