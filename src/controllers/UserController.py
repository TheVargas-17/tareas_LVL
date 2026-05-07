from models.UsersModel import UsuarioModel
from models.schemasModel import UsuarioShema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_Usuario(self, nombre, apellido, email, contraseña, telefono, fecha):
        try:
            nuevo_usuario = UsuarioShema(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=contraseña,
                telefono=telefono,
                fecha=fecha
            )

            success = self.model.registrar(nuevo_usuario)

            if success:
                return True, "Usuario creado correctamente"
            else:
                return False, "El usuario ya existe o hubo un error"

        except ValidationError as e:
            return False, e.errors()[0]['msg']

        except Exception as e:
            print("ERROR REGISTRO:", e)
            return False, "Error interno al registrar"

    def modificar(self, id_usuario, nombre, apellido, telefono):
        try:
            return self.model.modificar_perfil(id_usuario, nombre, apellido, telefono)

        except Exception as e:
            print("ERROR MODIFICAR:", e)
            return False

    def login(self, email, password):
        try:
            user = self.model.validar_login(email, password)

            if user:
                return user, "Login correcto"
            else:
                return None, "Credenciales incorrectas"

        except Exception as e:
            print("ERROR LOGIN:", e)
            return None, "Error en login"