from config import get_db_connection

class User:
    @staticmethod
    def get_all_users():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users

    @staticmethod
    def get_user_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def create_user(nombre, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (nombre, email) VALUES (%s, %s)', (nombre, email))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update_user(user_id, nombre, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET nombre = %s, email = %s WHERE id = %s', (nombre, email, user_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
