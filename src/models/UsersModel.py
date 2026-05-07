import bcrypt
from models.databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # verificar si existe
            cursor.execute(
                "SELECT * FROM usuario WHERE email=%s",
                (usuario_data.email,)
            )
            user = cursor.fetchone()

            if user:
                return False

            # hash password
            hashed_pw = bcrypt.hashpw(
                usuario_data.password.encode('utf-8'),
                bcrypt.gensalt()
            )

            cursor.execute(
                """
                INSERT INTO usuario 
                (nombre, apellido, email, contrasena, telefono, fecha_registro)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    usuario_data.nombre,
                    usuario_data.apellido,
                    usuario_data.email,
                    hashed_pw.decode('utf-8'),
                    usuario_data.telefono,
                    usuario_data.fecha
                )
            )

            conn.commit()
            return True

        except Exception as e:
            print("ERROR REGISTRO:", e)
            return False

        finally:
            conn.close()

    def modificar_perfil(self, id_usuario, nombre, apellido, telefono):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "UPDATE usuario SET nombre=%s WHERE id_usuario=%s",
                (nombre, id_usuario)
            )
            cursor.execute(
                "UPDATE usuario SET apellido=%s WHERE id_usuario=%s",
                (apellido, id_usuario)
            )
            cursor.execute(
                "UPDATE usuario SET telefono=%s WHERE id_usuario=%s",
                (telefono, id_usuario)
            )

            conn.commit()
            return True

        except Exception as e:
            print("ERROR MODIFICAR:", e)
            return False

        finally:
            conn.close()

    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT * FROM usuario WHERE email=%s",
                (email,)
            )
            user = cursor.fetchone()

            if not user:
                return None

            if bcrypt.checkpw(
                password.encode('utf-8'),
                user['contrasena'].encode('utf-8')
            ):
                cursor.execute(
                    """
                    UPDATE usuario 
                    SET ultimo_ingreso = NOW(), activo='activo'
                    WHERE id_usuario=%s
                    """,
                    (user["id_usuario"],)
                )

                conn.commit()
                return user

            return None

        except Exception as e:
            print("ERROR LOGIN:", e)
            return None

        finally:
            conn.close()

    def cerrar_sesion(self, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "UPDATE usuario SET activo='inactivo' WHERE id_usuario=%s",
                (id_usuario,)
            )

            conn.commit()

        except Exception as e:
            print("ERROR LOGOUT:", e)

        finally:
            conn.close()