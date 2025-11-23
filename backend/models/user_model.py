

from flask_bcrypt import generate_password_hash, check_password_hash
from database.connection import get_db_connection
import mysql.connector

class User:
    @staticmethod
    def create_user(name, email, password, phone=None):
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                hashed_password = generate_password_hash(password).decode('utf-8')
                
                query = """
                INSERT INTO customers (name, email, password, phone) 
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (name, email, hashed_password, phone))
                conn.commit()
                return True
            except Exception as err:
                print(f"Error creating user: {err}")
                return False
            finally:
                cursor.close()
                conn.close()
        return False

    @staticmethod
    def get_user_by_email(email):
        conn = get_db_connection()
        if conn:
            try:
                # Try to get dictionary cursor, fallback to regular cursor
                try:
                    cursor = conn.cursor(dictionary=True)
                except:
                    cursor = conn.cursor()
                
                query = "SELECT * FROM customers WHERE email = %s"
                cursor.execute(query, (email,))
                user = cursor.fetchone()
                
                # Convert to dictionary if needed
                if user and not isinstance(user, dict):
                    columns = [col[0] for col in cursor.description]
                    user = dict(zip(columns, user))
                
                return user
            except Exception as err:
                print(f"Error getting user: {err}")
                return None
            finally:
                cursor.close()
                conn.close()
        return None

    @staticmethod
    def verify_password(hashed_password, password):
        return check_password_hash(hashed_password, password)