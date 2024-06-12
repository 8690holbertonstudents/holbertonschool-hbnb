#!/usr/bin/python3
"""
"""
from flask import Blueprint, jsonify, request
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager
import json


amenity_bp = Blueprint('amenities', __name__)
data_manager = DataManager('app/storage/amenity.json')


@amenity_bp.route('/amenities/', methods=['GET'])
def get():
    """
    Retrieve amenities list
    """
    amenities = data_manager.get()
    if not amenities:
        return jsonify({'Error': 'amenity not found'}), 404
    return jsonify(amenities), 200


@amenity_bp.route('/amenities/', methods=['POST'])
def post():
    """
    Add a new amenity to amenities list
    """
    amenity_data = request.get_json()
    if not amenity_data:
        return jsonify({'Error': 'Bad request'}), 400
    name = amenity_data.get('name')
    if not name:
        return jsonify({'Error': 'No amenity name'}), 400
    new_amenity = Amenity(name)
    print(new_amenity.__dict__)
    if not new_amenity:
        return jsonify({'Error': 'Unable create new amenity'}), 400
    if not data_manager.save(new_amenity):
        return jsonify({'Error': 'Amenity exist or bad file'}), 409
    return jsonify({'Amenity added': name}), 200


@amenity_bp.route('/amenities/<string:amenity_id>/', methods=['GET'])
def get_id(amenity_id):
    """
    Retrieve amenity from id
    """
    amenity = data_manager.get_id(amenity_id)
    if not amenity:
        return jsonify({'Error': 'amenity not found'}), 404
    return jsonify(amenity), 200


def put_id(amenity_id):
    """
    Update amenity from id
    """
    pass


def delete_id(amenity_id):
    """
    Delete amenity from id
    """
    pass
