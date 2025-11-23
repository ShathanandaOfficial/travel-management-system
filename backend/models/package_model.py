
from database.connection import get_db_connection

class Package:
    @staticmethod
    def get_all_packages():
        conn = get_db_connection()
        if conn:
            try:
                # Try to get dictionary cursor, fallback to regular cursor
                try:
                    cursor = conn.cursor(dictionary=True)
                except:
                    cursor = conn.cursor()
                
                query = "SELECT * FROM travel_packages"
                cursor.execute(query)
                packages = cursor.fetchall()
                
                # Convert to list of dictionaries if needed
                if packages and not isinstance(packages[0], dict):
                    columns = [col[0] for col in cursor.description]
                    packages = [dict(zip(columns, row)) for row in packages]
                
                return packages
            except Exception as err:
                print(f"Error getting packages: {err}")
                return []
            finally:
                cursor.close()
                conn.close()
        return []

    @staticmethod
    def get_package_by_id(package_id):
        conn = get_db_connection()
        if conn:
            try:
                # Try to get dictionary cursor, fallback to regular cursor
                try:
                    cursor = conn.cursor(dictionary=True)
                except:
                    cursor = conn.cursor()
                
                query = "SELECT * FROM travel_packages WHERE package_id = %s"
                cursor.execute(query, (package_id,))
                package = cursor.fetchone()
                
                # Convert to dictionary if needed
                if package and not isinstance(package, dict):
                    columns = [col[0] for col in cursor.description]
                    package = dict(zip(columns, package))
                
                return package
            except Exception as err:
                print(f"Error getting package: {err}")
                return None
            finally:
                cursor.close()
                conn.close()
        return None

    @staticmethod
    def create_package(package_name, destination, price, description):
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                INSERT INTO travel_packages (package_name, destination, price, description) 
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (package_name, destination, price, description))
                conn.commit()
                return True
            except Exception as err:
                print(f"Error creating package: {err}")
                return False
            finally:
                cursor.close()
                conn.close()
        return False