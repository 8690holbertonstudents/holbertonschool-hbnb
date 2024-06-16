import os
import json
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes.amenity_routes import amenity_bp
from app.routes.user_routes import user_bp
from app.routes.city_routes import city_bp
from app.routes.country_routes import country_bp
from app.routes.review_routes import review_bp
from app.routes.place_routes import place_bp

app = Flask(__name__)


def load_data(id):
    storage_dir = 'storage'
    file_path = os.path.join(storage_dir, f'item{id}.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return None


# Register blueprints
app.register_blueprint(amenity_bp)
app.register_blueprint(user_bp)
app.register_blueprint(city_bp)
app.register_blueprint(country_bp)
app.register_blueprint(review_bp)
app.register_blueprint(place_bp)


@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = load_data(id)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404


# Define the Swagger UI blueprint
SWAGGER_URL = '/docs'  # URL for exposing Swagger UI
API_URL = '/static/swagger.yaml'  # Path to the OpenAPI spec file

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "HBNB API"
    }
)

# Register the Swagger UI blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
