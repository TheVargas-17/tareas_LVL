from models.schemasModel import UsuarioSchema
from models.UserModel import UsuarioModel
from pydantic import ValidationError


class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, email, password):
        try:
            # 🔥 Validar datos con Pydantic
            nuevo_usuario = UsuarioSchema(
                nombre=nombre,
                email=email,
                password=password
            )

            success = self.model.registrar(nuevo_usuario)

            if success:
                return True, "Usuario creado correctamente"
            else:
                return False, "Error al registrar usuario"

        except ValidationError as e:
            # 🔥 devolver primer error claro
            return False, e.errors()[0]['msg']

    def login(self, email, password):
        # 🔥 Validación básica
        if not email or not password:
            return None, "Llena todos los campos"

        user = self.model.validar_login(email, password)

        if user:
            return user, "Login correcto"
        else:
            return None, "Correo o contraseña incorrectos"