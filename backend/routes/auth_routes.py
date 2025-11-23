from flask import Blueprint, request, jsonify, session
from models.user_model import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        phone = data.get('phone')

        if not name or not email or not password:
            return jsonify({'error': 'Name, email and password are required'}), 400

        # Check if user already exists
        existing_user = User.get_user_by_email(email)
        if existing_user:
            return jsonify({'error': 'User already exists'}), 400

        # Create user
        if User.create_user(name, email, password, phone):
            return jsonify({'message': 'User registered successfully'}), 201
        else:
            return jsonify({'error': 'Failed to create user'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        user = User.get_user_by_email(email)
        if user and User.verify_password(user['password'], password):
            session['user_id'] = user['customer_id']
            session['user_name'] = user['name']
            session['user_email'] = user['email']
            session['is_admin'] = user.get('is_admin', False)
            
            return jsonify({
                'message': 'Login successful',
                'user': {
                    'id': user['customer_id'],
                    'name': user['name'],
                    'email': user['email'],
                    'is_admin': user.get('is_admin', False)
                }
            }), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully'}), 200