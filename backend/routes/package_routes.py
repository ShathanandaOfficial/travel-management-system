from flask import Blueprint, request, jsonify
from models.package_model import Package

package_bp = Blueprint('packages', __name__)

@package_bp.route('/packages', methods=['GET'])
def get_packages():
    try:
        packages = Package.get_all_packages()
        return jsonify(packages), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@package_bp.route('/packages', methods=['POST'])
def create_package():
    try:
        data = request.get_json()
        package_name = data.get('package_name')
        destination = data.get('destination')
        price = data.get('price')
        description = data.get('description')

        if not all([package_name, destination, price]):
            return jsonify({'error': 'Package name, destination and price are required'}), 400

        if Package.create_package(package_name, destination, price, description):
            return jsonify({'message': 'Package created successfully'}), 201
        else:
            return jsonify({'error': 'Failed to create package'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@package_bp.route('/packages/<int:package_id>', methods=['GET'])
def get_package(package_id):
    try:
        package = Package.get_package_by_id(package_id)
        if package:
            return jsonify(package), 200
        else:
            return jsonify({'error': 'Package not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500