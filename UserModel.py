import bcrypt
from .databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):
        # Encriptar contraseña
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)

        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, email, password) VALUES (%s, %s, %s)",
                (usuario_data.nombre, usuario_data.email, hashed_pw.decode())
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False