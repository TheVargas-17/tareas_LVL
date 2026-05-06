from models.schemasModel import UsuarioSchema
from models.UserModel import UsuarioModel
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, email, password):
        try:
            # Validar datos
            nuevo_usuario = UsuarioSchema(
                nombre=nombre,
                email=email,
                password=password
            )

          
            if self.model.buscar_por_email(email):
                return False, "El usuario ya existe"

            success = self.model.registrar(nuevo_usuario)

            if success:
                return True, "Usuario creado correctamente"
            else:
                return False, "Error al registrar usuario"

        except ValidationError as e:
            return False, e.errors()[0]['msg']

    def login(self, email, password):
        user = self.model.validar_login(email, password)

        if user:
            return user, "Login correcto "
        else:
            return None, "Correo o contraseña incorrectos "