#!/usr/bin/python3
"""
python module for amenity routes
"""
from flask import Blueprint, jsonify, request, abort
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager


amenity_bp = Blueprint('amenities', __name__)
data_manager = DataManager('app/storage/amenity.json')


def common_check(amenity_data):
    """
    Common check for POST and PUT
    """
    if not amenity_data:
        return jsonify({'Error': 'Bad request, no data'}), 400

    if not isinstance(amenity_data, dict):
        return jsonify({'Error': 'amenity is not JSON object'}), 400

    if 'name' not in amenity_data:
        return jsonify({'Error': 'amenity must have a name'}), 400

    if not isinstance(amenity_data['name'], str):
        return jsonify({'Error': 'amenity name is not a string'}), 400

    if len(amenity_data['name']) == 0:
        return jsonify({'Error': 'amenity name cannot be empty'}), 400

    return None


def get_amenity_data():
    """
    Get amenity data from request
    """
    try:
        amenity_data = request.get_json()
    except:
        return jsonify({'Error': 'Bad JSON object'}), 400

    return amenity_data


@amenity_bp.route('/amenities', methods=['GET'])
def get():
    """
    Retrieve amenities list with GET
    """
    amenities = data_manager.get()

    if amenities is None:
        amenities = []

    if amenities is False:
        return jsonify({'Error': 'amenities not found'}), 404

    if request.method == 'GET':
        return jsonify(amenities), 200

    if request.method == 'POST' or request.method == 'PUT':
        return amenities


@amenity_bp.route('/amenities', methods=['POST'])
def post():
    """
    Add a new amenity to amenities list with POST
    """
    amenities = get()

    amenity_data = get_amenity_data()

    err_check = common_check(amenity_data)
    if err_check:
        return err_check

    for item in amenities:
        if item['name'] == amenity_data['name']:
            return jsonify({'Error': 'amenity name already exist'}), 409

    name = amenity_data.get('name')
    new_amenity = Amenity(name)
    if not new_amenity:
        return jsonify({'Error': 'unable create new amenity'}), 400

    new_amenity.__dict__['amenity_id'] = new_amenity.__dict__.pop('id')
    if data_manager.save(new_amenity.__dict__) is False:
        return jsonify({'Error': 'bad json file'}), 409
    return jsonify({'amenity added': name}), 200


@amenity_bp.route('/amenities/<string:amenity_id>', methods=['GET'])
def get_id(amenity_id):
    """
    Retrieve amenity from id with GET
    """
    amenity = data_manager.get_id(amenity_id)
    if amenity is False:
        return abort(404)

    if request.method == 'GET':
        return jsonify(amenity), 200

    if request.method == 'PUT' or request.method == 'DELETE':
        return amenity


@amenity_bp.route('/amenities/<string:amenity_id>', methods=['PUT'])
def put_id(amenity_id):
    """
    Updade amenity from id with PUT
    """
    amenities = get()
    amenity = get_id(amenity_id)

    amenity_data = get_amenity_data()

    err_check = common_check(amenity_data)
    if err_check:
        return err_check

    for item in amenities:
        if item['name'] == amenity_data['name']:
            return jsonify({'Error': 'amenity name already exist'}), 409

    amenity['name'] = amenity_data['name']
    data_manager.update('amenity_id', amenity)
    return jsonify({'amenity updated': amenity['name']}), 200


@amenity_bp.route('/amenities/<string:amenity_id>', methods=['DELETE'])
def delete_id(amenity_id):
    """
    Delete amenity from id with DELETE
    """
    amenity = get_id(amenity_id)

    data_manager.delete('amenity_id', amenity)
    return jsonify({'amenity deleted': amenity['name']}), 200


@amenity_bp.app_errorhandler(404)
def not_found(error):
    """
    Handle err 404 for undefined routes
    """
    return jsonify({'Error': 'Bad url'}), 404
