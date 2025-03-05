from database import get_db_connection

class Usuario:
    def __init__(self, id=None, nombre=None, email=None):
        self.id = id
        self.nombre = nombre
        self.email = email

    @staticmethod
    def obtener_todos():
        conexion = get_db_connection()
        if not conexion:
            return {"error": "Error de conexión a la base de datos"}

        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall()
            return usuarios
        except Exception as e:
            return {"error": str(e)}
        finally:
            conexion.close()

    @staticmethod
    def obtener_por_id(id):
        conexion = get_db_connection()
        if not conexion:
            return None

        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
            usuario = cursor.fetchone()
            return usuario
        except Exception as e:
            return {"error": str(e)}
        finally:
            conexion.close()

    def guardar(self):
        conexion = get_db_connection()
        if not conexion:
            return {"error": "Error de conexión a la base de datos"}

        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", (self.nombre, self.email))
            conexion.commit()
            return {"mensaje": "Usuario creado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            conexion.close()

    def actualizar(self):
        conexion = get_db_connection()
        if not conexion:
            return {"error": "Error de conexión a la base de datos"}

        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s", (self.nombre, self.email, self.id))
            conexion.commit()
            return {"mensaje": "Usuario actualizado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            conexion.close()

    @staticmethod
    def eliminar(id):
        conexion = get_db_connection()
        if not conexion:
            return {"error": "Error de conexión a la base de datos"}

        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
            conexion.commit()
            return {"mensaje": "Usuario eliminado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            conexion.close()
