

from database.connection import get_db_connection

class Booking:
    @staticmethod
    def create_booking(customer_id, package_id, travellers, total_price):
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                INSERT INTO bookings (customer_id, package_id, travellers, total_price) 
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (customer_id, package_id, travellers, total_price))
                conn.commit()
                return True
            except Exception as err:
                print(f"Error creating booking: {err}")
                return False
            finally:
                cursor.close()
                conn.close()
        return False

    @staticmethod
    def get_all_bookings():
        conn = get_db_connection()
        if conn:
            try:
                # Try to get dictionary cursor, fallback to regular cursor
                try:
                    cursor = conn.cursor(dictionary=True)
                except:
                    cursor = conn.cursor()
                
                query = """
                SELECT b.booking_id, b.travellers, b.total_price, 
                       c.name as customer_name, c.email,
                       p.package_name, p.destination
                FROM bookings b
                JOIN customers c ON b.customer_id = c.customer_id
                JOIN travel_packages p ON b.package_id = p.package_id
                ORDER BY b.booking_id DESC
                """
                cursor.execute(query)
                bookings = cursor.fetchall()
                
                # Convert to list of dictionaries if needed
                if bookings and not isinstance(bookings[0], dict):
                    columns = [col[0] for col in cursor.description]
                    bookings = [dict(zip(columns, row)) for row in bookings]
                
                return bookings
            except Exception as err:
                print(f"Error getting bookings: {err}")
                return []
            finally:
                cursor.close()
                conn.close()
        return []