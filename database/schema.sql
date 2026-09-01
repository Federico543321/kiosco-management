CREATE DATABASE kiosco_management;
USE kiosco_management;

CREATE TABLE negocio (
    id_negocio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200)
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(150),
    telefono VARCHAR(30),
    estado VARCHAR(20) NOT NULL
);

CREATE TABLE usuario_negocio (
    id_usuario_negocio INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_negocio INT NOT NULL,
    rol VARCHAR(20) NOT NULL,
    estado VARCHAR(20) NOT NULL,

    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio),

    UNIQUE (id_usuario, id_negocio)
);

CREATE TABLE invitacion (
    id_invitacion INT AUTO_INCREMENT PRIMARY KEY,
    id_negocio INT NOT NULL,
    codigo_generado VARCHAR(50) NOT NULL UNIQUE,
    estado VARCHAR(20) NOT NULL,
    fecha_creacion DATETIME NOT NULL,
    fecha_expiracion DATETIME NOT NULL,

    FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio)
);

CREATE TABLE suscripcion (
    id_suscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_negocio INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_vencimiento DATE NOT NULL,
    estado VARCHAR(20) NOT NULL,

    FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio)
);

CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    id_negocio INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    estado VARCHAR(20) NOT NULL,

    UNIQUE (id_negocio, nombre),

    FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio)
);

CREATE TABLE producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    id_negocio INT NOT NULL,
    id_categoria INT NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    marca VARCHAR(100),
    presentacion_gramaje VARCHAR(50),
    codigo_barras VARCHAR(50),
    precio_venta DECIMAL(10,2) NOT NULL,
    stock_minimo INT NOT NULL DEFAULT 0,
    estado VARCHAR(20) NOT NULL,

    FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

CREATE TABLE lote (
    id_lote INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    cantidad_inicial INT NOT NULL,
    cantidad_disponible INT NOT NULL,
    costo_unitario DECIMAL(10,2) NOT NULL,
    fecha_ingreso DATETIME NOT NULL,

    FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

CREATE TABLE modo_pago (
    id_modo_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_negocio INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    estado VARCHAR(20) NOT NULL,

    UNIQUE (id_negocio, nombre),

    FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio)
);

CREATE TABLE venta (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_negocio INT NOT NULL,
    id_usuario INT NOT NULL,
    id_modo_pago INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    dinero_recibido DECIMAL(10,2),
    vuelto DECIMAL(10,2),

    FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_modo_pago) REFERENCES modo_pago(id_modo_pago)
);

CREATE TABLE detalle_venta (
    id_detalle_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (id_venta) REFERENCES venta(id_venta),
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

CREATE TABLE detalle_venta_lote (
    id_detalle_venta_lote INT AUTO_INCREMENT PRIMARY KEY,
    id_detalle_venta INT NOT NULL,
    id_lote INT NOT NULL,
    cantidad INT NOT NULL,
    costo_unitario DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (id_detalle_venta) REFERENCES detalle_venta(id_detalle_venta),
    FOREIGN KEY (id_lote) REFERENCES lote(id_lote)
);

CREATE TABLE motivo_movimiento (
    id_motivo INT AUTO_INCREMENT PRIMARY KEY,
    id_negocio INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    estado VARCHAR(20) NOT NULL,

    UNIQUE (id_negocio, nombre),

    FOREIGN KEY (id_negocio) REFERENCES negocio(id_negocio)
);

CREATE TABLE movimiento_stock (
    id_movimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    id_usuario INT NOT NULL,
    id_motivo INT NOT NULL,
    cantidad INT NOT NULL,
    observacion VARCHAR(255),
    fecha_hora DATETIME NOT NULL,

    FOREIGN KEY (id_producto) REFERENCES producto(id_producto),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_motivo) REFERENCES motivo_movimiento(id_motivo)
);

CREATE TABLE movimiento_stock_lote (
    id_movimiento_stock_lote INT AUTO_INCREMENT PRIMARY KEY,
    id_movimiento INT NOT NULL,
    id_lote INT NOT NULL,
    cantidad INT NOT NULL,

    FOREIGN KEY (id_movimiento) REFERENCES movimiento_stock(id_movimiento),
    FOREIGN KEY (id_lote) REFERENCES lote(id_lote)
);

CREATE TABLE auditoria (
    id_auditoria INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    tipo_entidad VARCHAR(50) NOT NULL,
    id_registro INT NOT NULL,
    accion VARCHAR(30) NOT NULL,
    detalle VARCHAR(255),
    valor_anterior TEXT,
    valor_nuevo TEXT,
    motivo VARCHAR(255),
    fecha_hora DATETIME NOT NULL,

    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);