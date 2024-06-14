#!/usr/bin/python3
"""
"""
from flask import Blueprint, jsonify, request, abort
from app.models.user import User
from app.persistence.data_manager import DataManager
import re


user_bp = Blueprint('users', __name__)
data_manager = DataManager('app/storage/user.json')


def str_email_check(email):
    """
    Check email string content (not a real validation).
    """
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    return re.match(email_regex, email) is not None


def common_check(user_data):
    """
    Common check for POST and PUT
    """
    if not user_data:
        return jsonify({'Error': 'Bad request, no data'}), 400

    if not isinstance(user_data, dict):
        return jsonify({'Error': 'user is not JSON object'}), 400

    if 'email' not in user_data or len(user_data['email']) == 0:
        return jsonify({'Error': 'user must have an email'}), 400

    if not str_email_check(user_data['email']):
        return jsonify({'Error': 'email string is not valid'}), 400

    if 'first_name' not in user_data or len(user_data['first_name']) == 0:
        return jsonify({'Error': 'user must have a first_name'}), 400

    if 'last_name' not in user_data or len(user_data['last_name']) == 0:
        return jsonify({'Error': 'user must have a last_name'}), 400

    if len(user_data) != 3:
        return jsonify({'Error': 'user must contain 3 elements'}), 400

    if not isinstance(user_data['email'], str) \
            or not isinstance(user_data['first_name'], str) \
            or not isinstance(user_data['last_name'], str):
        return jsonify({'Error': 'request data must be string'}), 400

    return None


def get_user_data():
    """
    Get user data from request
    """
    try:
        user_data = request.get_json()
    except:
        return jsonify({'Error': 'Bad JSON object'}), 400

    return user_data


@user_bp.route('/users/', methods=['GET'])
def get():
    """
    Retrieve users list with GET
    """
    users = data_manager.get()

    if users is None:
        users = []

    if users is False:
        return jsonify({'Error': 'users not found'}), 404

    if request.method == 'GET':
        return jsonify(users), 200

    if request.method == 'POST' or request.method == 'PUT':
        return users


@user_bp.route('/users/', methods=['POST'])
def post():
    """
    Add a new user to users list with POST
    """
    users = get()

    user_data = get_user_data()

    err_check = common_check(user_data)
    if err_check:
        return err_check

    for item in users:
        if item['email'] == user_data['email']:
            return jsonify({'Error': 'user email already exist'}), 409

    email = user_data.get('email')
    first_name = user_data.get('first_name')
    last_name = user_data.get('last_name')

    new_user = User(email, first_name, last_name)
    if not new_user:
        return jsonify({'Error': 'unable create new user'}), 400

    new_user.__dict__['user_id'] = new_user.__dict__.pop('id')
    if data_manager.save(new_user.__dict__) is False:
        return jsonify({'Error': 'bad json file'}), 409
    return jsonify({'user added': email}), 200


@user_bp.route('/users/<string:user_id>/', methods=['GET'])
def get_id(user_id):
    """
    Retrieve user from id with GET
    """
    user = data_manager.get_id(user_id)
    if user is False:
        return abort(404)

    if request.method == 'GET':
        return jsonify(user), 200

    if request.method == 'PUT' or request.method == 'DELETE':
        return user


@user_bp.route('/users/<string:user_id>/', methods=['PUT'])
def put_id(user_id):
    """
    Updade user from id with PUT
    """
    users = get()
    user = get_id(user_id)

    user_data = get_user_data()

    err_check = common_check(user_data)
    if err_check:
        return err_check

    for item in users:
        if item['email'] == user_data['email'] and item['user_id'] != user_id:
            return jsonify({'Error': 'user email already exist'}), 409

    user['email'] = user_data['email']
    user['first_name'] = user_data['first_name']
    user['last_name'] = user_data['last_name']
    data_manager.update('user_id', user)
    return jsonify({'user updated': user['email']}), 200


@user_bp.route('/users/<string:user_id>/', methods=['DELETE'])
def delete_id(user_id):
    """
    Delete user from id with DELETE
    """
    user = get_id(user_id)

    data_manager.delete('user_id', user)
    return jsonify({'user deleted': user['email']}), 200


@user_bp.app_errorhandler(404)
def not_found(error):
    """
    Handle err 404 for undefined routes
    """
    return jsonify({'Error': 'Bad url'}), 404
