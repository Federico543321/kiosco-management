class Usuario:
    def __init__(
        self,
        id_usuario=None,
        nombre=None,
        nombre_usuario=None,
        password_hash=None,
        email=None,
        telefono=None,
        estado=None
    ):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.nombre_usuario = nombre_usuario
        self.password_hash = password_hash
        self.email = email
        self.telefono = telefono
        self.estado = estado