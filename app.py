#!/usr/bin/python3
"""
"""
from flask import Flask
from flask_restx import Api
from app.routes import amenity_ns, city_ns, country_ns, place_ns, review_ns, user_ns


app = Flask(__name__)
api = Api(app, version='1.0', title='My API', description='A simple API')


api.add_namespace(amenity_ns, path='/amenities')
api.add_namespace(city_ns, path='/cities')
api.add_namespace(country_ns, path='/countries')
api.add_namespace(place_ns, path='/places')
api.add_namespace(review_ns, path='/reviews')
api.add_namespace(user_ns, path='/users')

if __name__ == '__main__':
    app.run()
