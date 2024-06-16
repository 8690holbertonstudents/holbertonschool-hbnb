#!/usr/bin/python3
"""
python module for country / city routes
"""
from flask import Blueprint, jsonify, request
from app.models.city import City
from app.routes.country_routes import get_country_details
from app.routes.manager_routes import get_request_data
from app.persistence.data_manager import DataManager
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError


city_bp = Blueprint('cities', __name__)
data_manager = DataManager('storage/city.json')


def check_geolocator(name):
    """
    Check geolocator for city name
    """
    geolocator = Nominatim(user_agent="city_app")
    try:
        location = geolocator.geocode(name)
        if location is None:
            return False
    except GeopyError as e:
        return jsonify({'Error': f'Geocoding error: {str(e)}'}), 500

    return True


@ city_bp.route('/cities', methods=['GET'])
def get_cities():
    """
    Retrieve cities list with GET
    """
    cities = data_manager.get()

    if cities is None:
        cities = []

    if cities is False:
        return jsonify({'Error': 'cities not found'}), 404

    if request.method == 'GET':
        return jsonify(cities), 200
    else:
        return cities, 200


@ city_bp.route('/cities', methods=['POST'])
def post():
    """
    Add a new city to cities list with POST
    """
    cities_response = get_cities()
    cities = cities_response[0]

    city_data = get_request_data()

    err_check = City.data_check(city_data)
    if err_check:
        return err_check

    name = city_data.get('name')
    name = name[0].upper() + name[1:].lower()

    for item in cities:
        if item['name'] == name:
            return jsonify({'Error': 'city name already exist'}), 409

    if check_geolocator(name) is False:
        return jsonify({'Error': 'City not on earth !'}), 400

    country_details, status_code = get_country_details(
        city_data.get('country_code'))
    if status_code != 200:
        return jsonify(country_details), status_code
    else:
        country_code = country_details.get('alpha2')

    new_city = City(country_code, name)
    if not new_city:
        return jsonify({'Error': 'unable create new city'}), 400

    new_city.__dict__['city_id'] = new_city.__dict__.pop('id')
    if data_manager.save(new_city.__dict__) is False:
        return jsonify({'Error': 'bad json file'}), 409
    return jsonify({'city added': name}), 200


@ city_bp.route('/cities/<string:city_id>', methods=['GET'])
def get_id(city_id):
    """
    Retrieve city from id with GET
    """
    city = data_manager.get_id(city_id)
    if city is False:
        return jsonify({'Error': 'city not found'}), 404

    if request.method == 'GET':
        return jsonify(city), 200

    if request.method == 'PUT' or request.method == 'DELETE':
        return city


@ city_bp.route('/cities/<string:city_id>', methods=['PUT'])
def put_id(city_id):
    """
    Updade city from id with PUT
    """
    city = get_id(city_id)

    city_data = get_request_data()

    err_check = City.data_check(city_data)
    if err_check:
        return err_check

    cities_response = get_cities()
    cities = cities_response[0]

    name = city_data.get('name')
    name = name[0].upper() + name[1:].lower()

    for item in cities:
        if item['name'] == name:
            return jsonify({'Error': 'city name already exist'}), 409

    if check_geolocator(name) is False:
        return jsonify({'Error': 'City not on earth !'}), 400

    country_details, status_code = get_country_details(
        city_data.get('country_code'))
    if status_code != 200:
        return jsonify(country_details), status_code
    else:
        country_code = country_details.get('alpha2')

    city['name'] = name
    city['country_code'] = country_code
    data_manager.update('city_id', city)
    return jsonify({'city updated': city['name']}), 200


@ city_bp.route('/cities/<string:city_id>', methods=['DELETE'])
def delete_id(city_id):
    """
    Delete city from id with DELETE
    """
    city = get_id(city_id)

    data_manager.delete('city_id', city)
    return jsonify({'city deleted': city['name']}), 200
