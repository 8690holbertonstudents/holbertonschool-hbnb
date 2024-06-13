#!/usr/bin/python3
"""
"""
from flask import Blueprint, jsonify, request
from app.models.user import User
from app.persistence.data_manager import DataManager


user_bp = Blueprint('users', __name__)
data_manager = DataManager('app/storage/user.json')


@user_bp.route('/users/', methods=['GET'])
def get():
    """
    Retrieve users list with GET
    """
    users = data_manager.get()
    if not users:
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
    user_data = request.get_json()
    if not user_data:
        return jsonify({'Error': 'bad request'}), 400

    email = user_data.get('email')
    if not email:
        return jsonify({'Error': 'no user email'}), 400

    first_name = user_data.get('first_name')
    if not first_name or type(first_name) is not str:
        return jsonify({'Error': 'no user first_name or not string'}), 400

    last_name = user_data.get('last_name')
    if not last_name or type(last_name) is not str:
        return jsonify({'Error': 'no user last_name or not string'}), 400

    for item in users:
        if item['email'] == user_data['email']:
            return jsonify({'Error': 'user email already exist'}), 409

    new_user = User(email, first_name, last_name)
    if not new_user:
        return jsonify({'Error': 'unable create new user'}), 400

    new_user.__dict__['user_id'] = new_user.__dict__.pop('id')
    if not data_manager.save(new_user.__dict__):
        return jsonify({'Error': 'bad json file'}), 409
    return jsonify({'user added': email}), 200


@user_bp.route('/users/<string:user_id>/', methods=['GET'])
def get_id(user_id):
    """
    Retrieve user from id with GET
    """

    user = data_manager.get_id(user_id)
    if not user:
        return jsonify({'Error': 'user not found'}), 404

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
    if not users:
        return jsonify({'Error': 'users not found'}), 404

    user = get_id(user_id)
    if not user:
        return jsonify({'Error': 'user not found'}), 404

    user_data = request.get_json()
    if not user_data:
        return jsonify({'Error': 'user not found'}), 404

    for item in users:
        if item['email'] == user_data['email']:
            return jsonify({'Error': 'user email already exist'}), 409

    user['name'] = user_data['name']
    data_manager.update('user_id', user)
    return jsonify({'user updated': user['name']}), 200


@user_bp.route('/users/<string:user_id>/', methods=['DELETE'])
def delete_id(user_id):
    """
    Delete user from id with DELETE
    """

    user = get_id(user_id)
    if not user:
        return jsonify({'Error': 'user not found'}), 404

    data_manager.delete('user_id', user)
    return jsonify({'user deleted': user['email']}), 200
