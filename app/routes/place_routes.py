#!/usr/bin/python3
"""
python module for places routes
"""
from flask import Blueprint, jsonify, request
from app.persistence.data_manager import DataManager


place_bp = Blueprint('places', __name__)
data_manager = DataManager('app/storage/place.json')


@place_bp.route('/places', methods=['GET'])
def get_places():
    """
    Retrieve places list with GET
    """
    places = data_manager.get()

    if places is None:
        places = []

    if places is False:
        return jsonify({'Error': 'amenities not found'}), 404

    if request.method == 'GET':
        return jsonify(places), 200

    # if request.method == 'POST' or request.method == 'PUT':
        # return amenities


@place_bp.route('/places/<string:place_id>', methods=['GET'])
def get_places_id(place_id):
    """
    Retrieve place from id with GET
    """
    place = data_manager.get_id(place_id)
    if place is False:
        return jsonify({'Error': 'amenity not found'}), 404

    if request.method == 'GET':
        return jsonify(place), 200

    # if request.method == 'PUT' or request.method == 'DELETE':
        # return place
