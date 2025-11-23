from flask import Blueprint, request, jsonify, session
from models.booking_model import Booking
from models.package_model import Package

booking_bp = Blueprint('bookings', __name__)

@booking_bp.route('/bookings', methods=['POST'])
def create_booking():
    try:
        if 'user_id' not in session:
            return jsonify({'error': 'Please login to book a package'}), 401

        data = request.get_json()
        package_id = data.get('package_id')
        travellers = data.get('travellers')

        if not package_id or not travellers:
            return jsonify({'error': 'Package ID and number of travellers are required'}), 400

        # Get package details
        package = Package.get_package_by_id(package_id)
        if not package:
            return jsonify({'error': 'Package not found'}), 404

        # Calculate total price
        total_price = package['price'] * travellers

        # Create booking
        if Booking.create_booking(session['user_id'], package_id, travellers, total_price):
            return jsonify({'message': 'Booking created successfully'}), 201
        else:
            return jsonify({'error': 'Failed to create booking'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@booking_bp.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        # For admin, show all bookings; for users, show only their bookings
        # This is a simplified version - in real app, add user-specific filtering
        bookings = Booking.get_all_bookings()
        return jsonify(bookings), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500