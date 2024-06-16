#!/usr/bin/python3
"""
python module for amenity routes
"""
from flask import Blueprint, jsonify, request
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager
from app.routes.manager_routes import get_request_data

amenity_bp = Blueprint('amenities', __name__)
data_manager = DataManager('app/storage/amenity.json')


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

    amenity_data = get_request_data()

    err_check = Amenity.data_check(amenity_data)
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
        return jsonify({'Error': 'amenity not found'}), 404

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

    amenity_data = get_request_data()

    err_check = Amenity.data_check(amenity_data)
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

