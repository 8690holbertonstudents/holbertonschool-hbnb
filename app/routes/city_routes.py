#!/usr/bin/python3
"""
python module for country / city routes
"""
from flask import Blueprint, jsonify, request, abort
from app.models.city import City
from app.persistence.data_manager import DataManager
import pycountry
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError


city_bp = Blueprint('cities', __name__)
data_manager = DataManager('app/storage/city.json')


@city_bp.route('/countries', methods=['GET'])
def get_countries():
    """
    Retrieve countries list with GET from ISO 3166-2
    """
    try:
        countries_data = {}
        for country in pycountry.countries:
            countries_data[country.name] = country.alpha_2
        return jsonify(countries_data), 200

    except Exception as e:
        return jsonify({'Error': str(e)}), 500


def get_country_details(country_code):
    """
    Retrieve country details by code from ISO 3166-2
    """
    country_code = country_code.upper()
    if len(country_code) != 2:
        return {'Error': 'country code must be 2 letters'}, 400

    country_details = {}
    for country in pycountry.countries:
        if country.alpha_2 == country_code:
            country_details['name'] = country.name
            country_details['alpha2'] = country.alpha_2
            country_details['alpha3'] = country.alpha_3
            country_details['numeric'] = country.numeric
            return country_details, 200

    return {'Error': 'No valid country code'}, 404


@ city_bp.route('/countries/<country_code>', methods=['GET'])
def get_country_code(country_code):
    """
    Retrieve country details by code with GET
    """
    try:
        country_details, status_code = get_country_details(country_code)
        return jsonify(country_details), status_code
    except Exception as e:
        return jsonify({'Error': str(e)}), 500


def common_check(city_data):
    """
    Common check for POST and PUT
    """
    if not city_data:
        return jsonify({'Error': 'Bad request, no data'}), 400

    if not isinstance(city_data, dict):
        return jsonify({'Error': 'city is not JSON object'}), 400

    if 'name' not in city_data:
        return jsonify({'Error': 'city must have a name'}), 400

    if not isinstance(city_data['name'], str):
        return jsonify({'Error': 'city name is not a string'}), 400

    if len(city_data['name']) == 0:
        return jsonify({'Error': 'city name cannot be empty'}), 400

    return None


def get_city_data():
    """
    Get city data from request
    """
    try:
        city_data = request.get_json()
    except:
        return jsonify({'Error': 'Bad JSON object'}), 400

    return city_data


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
def get():
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

    if request.method == 'POST' or request.method == 'PUT':
        return cities


@ city_bp.route('/cities', methods=['POST'])
def post():
    """
    Add a new city to cities list with POST
    """
    cities = get()

    city_data = get_city_data()

    err_check = common_check(city_data)
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
        return abort(404)

    if request.method == 'GET':
        return jsonify(city), 200

    if request.method == 'PUT' or request.method == 'DELETE':
        return city


@ city_bp.route('/cities/<string:city_id>', methods=['PUT'])
def put_id(city_id):
    """
    Updade city from id with PUT
    """
    cities = get()
    city = get_id(city_id)

    city_data = get_city_data()

    err_check = common_check(city_data)
    if err_check:
        return err_check

    for item in cities:
        if item['name'].lower() == city_data['name'].lower():
            return jsonify({'Error': 'city name already exist'}), 409

    name = city_data.get('name')
    name = name[0].upper() + name[1:].lower()

    check_geolocator(name)

    city['name'] = name
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


@ city_bp.app_errorhandler(404)
def not_found(error):
    """
    Handle err 404 for undefined routes
    """
    return jsonify({'Error': 'Bad url'}), 404
