import bcrypt
from models.databaseModel import Database 
class UsuarioModel:
    def __init__(self):
        self.db = Database()

    # ✅ REGISTRAR USUARIO
    def registrar(self, usuario_data):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)

        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, email, password) VALUES (%s, %s, %s)",
                (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))
            )
            conn.commit()
            return True

        except Exception as e:
            print(f"Error: {e}")
            return False

        finally:
            conn.close()

    # ✅ VALIDAR LOGIN
    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuario WHERE email = %s",
            (email,)
        )
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(
            password.encode('utf-8'),
            user['password'].encode('utf-8')
        ):
            return user

        return None

    # 🔥 NUEVO → BUSCAR USUARIO POR EMAIL
    def buscar_por_email(self, email):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM usuario WHERE email = %s",
            (email,)
        )

        result = cursor.fetchone()
        conn.close()

        return result is not None