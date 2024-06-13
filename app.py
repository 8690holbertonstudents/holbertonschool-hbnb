#!/usr/bin/python3
"""
"""
from flask import Flask
from app.routes.amenity_routes import amenity_bp
from app.routes.user_routes import user_bp


app = Flask(__name__)

app.register_blueprint(amenity_bp)
app.register_blueprint(user_bp)


@app.route('/')
def home():
    """
    Start route '/'
    """
    return 'Holberton-hbnb API'


if __name__ == '__main__':
    app.run(debug=True)
