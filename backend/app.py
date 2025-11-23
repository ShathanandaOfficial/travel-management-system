
from flask import Flask, session, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from config import Config
from routes.auth_routes import auth_bp
from routes.package_routes import package_bp
from routes.booking_routes import booking_bp

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

# Initialize extensions
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])
bcrypt = Bcrypt(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(package_bp, url_prefix='/api')
app.register_blueprint(booking_bp, url_prefix='/api')

# Create database tables (initial setup)
def create_tables():
    try:
        from database.connection import get_db_connection
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            
            # Create customers table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    phone VARCHAR(20),
                    is_admin BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create travel_packages table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS travel_packages (
                    package_id INT AUTO_INCREMENT PRIMARY KEY,
                    package_name VARCHAR(100) NOT NULL,
                    destination VARCHAR(100) NOT NULL,
                    price DECIMAL(10, 2) NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create bookings table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS bookings (
                    booking_id INT AUTO_INCREMENT PRIMARY KEY,
                    customer_id INT,
                    package_id INT,
                    travellers INT NOT NULL,
                    total_price DECIMAL(10, 2) NOT NULL,
                    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
                    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id) ON DELETE CASCADE
                )
            """)
            
            # Insert sample data
            cursor.execute("SELECT COUNT(*) FROM travel_packages")
            result = cursor.fetchone()
            # Handle different cursor return types
            count = result[0] if isinstance(result, (list, tuple)) else result['COUNT(*)'] if isinstance(result, dict) else result[0]
            
            if count == 0:
                sample_packages = [
                    ('Beach Paradise', 'Maldives', 1200.00, 'Enjoy 5 days in beautiful Maldives with all inclusive resort'),
                    ('Mountain Trek', 'Switzerland', 800.00, '7-day hiking adventure in Swiss Alps'),
                    ('City Explorer', 'Paris', 600.00, '4-day cultural tour of Paris landmarks'),
                    ('Desert Safari', 'Dubai', 950.00, '3-day desert adventure with luxury camping')
                ]
                
                for package in sample_packages:
                    cursor.execute(
                        "INSERT INTO travel_packages (package_name, destination, price, description) VALUES (%s, %s, %s, %s)",
                        package
                    )
                
                # Create a default admin user
                from models.user_model import User
                User.create_user('Admin User', 'admin@travel.com', 'admin123', '1234567890')
                
                # Set admin flag
                cursor.execute("UPDATE customers SET is_admin = TRUE WHERE email = 'admin@travel.com'")
            
            conn.commit()
            cursor.close()
            conn.close()
            print("✅ Database tables created successfully!")
            
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

# Create tables when app starts
with app.app_context():
    create_tables()

@app.route('/')
def home():
    return jsonify({'message': 'Travel Management System API is running!'})

@app.route('/api/check-auth')
def check_auth():
    if 'user_id' in session:
        return jsonify({
            'authenticated': True,
            'user': {
                'id': session['user_id'],
                'name': session['user_name'],
                'email': session['user_email'],
                'is_admin': session.get('is_admin', False)
            }
        }), 200
    else:
        return jsonify({'authenticated': False}), 401

if __name__ == '__main__':
    print("🚀 Starting Travel Management System Backend...")
    print("📊 Database initialization completed!")
    print("🌐 Server running on http://localhost:5000")
    app.run(debug=True, port=5000)