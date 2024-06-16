#!/usr/bin/python3
"""
python module for country / city routes
"""
from flask import Blueprint, jsonify
from app.persistence.data_manager import DataManager
import pycountry


country_bp = Blueprint('countries', __name__)
data_manager = DataManager('app/storage/city.json')


@country_bp.route('/countries', methods=['GET'])
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


@ country_bp.route('/countries/<country_code>', methods=['GET'])
def get_country_code(country_code):
    """
    Retrieve country details by code with GET
    """
    try:
        country_details, status_code = get_country_details(country_code)
        return jsonify(country_details), status_code
    except Exception as e:
        return jsonify({'Error': str(e)}), 500


@ country_bp.route('/countries/<country_code>/cities', methods=['GET'])
def get_city_country(country_code):
    """
    Retrieve cities list by country code with GET
    """
    cities = data_manager.get()

    if cities is None:
        cities = []

    if cities is False:
        return jsonify({'Error': 'cities not found'}), 404

    country_code = country_code.upper()
    if len(country_code) != 2:
        return jsonify({'Error': 'country code must be 2 letters'}), 400

    city_names = []
    for city in cities:
        if city['country_code'] == country_code:
            city_names.append(city['name'])

    if len(city_names) == 0:
        return jsonify({'Error': 'No cities found for the given country code'}), 404

    return jsonify(city_names), 200
