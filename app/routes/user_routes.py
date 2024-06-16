#!/usr/bin/python3
"""
python module for user routes
"""
from flask import Blueprint, jsonify, request
from app.models.user import User
from app.persistence.data_manager import DataManager
from app.routes.manager_routes import get_request_data


user_bp = Blueprint('users', __name__)
data_manager = DataManager('storage/user.json')


@user_bp.route('/users', methods=['GET'])
def get_users():
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


@user_bp.route('/users', methods=['POST'])
def post():
    """
    Add a new user to users list with POST
    """
    users = get_users()

    user_data = get_request_data()

    err_check = User.data_check(user_data)
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


@user_bp.route('/users/<string:user_id>', methods=['GET'])
def get_id(user_id):
    """
    Retrieve user from id with GET
    """
    user = data_manager.get_id(user_id)
    if user is False:
        return jsonify({'Error': 'user not found'}), 404

    if request.method == 'GET':
        return jsonify(user), 200

    if request.method == 'PUT' or request.method == 'DELETE':
        return user


@user_bp.route('/users/<string:user_id>', methods=['PUT'])
def put_id(user_id):
    """
    Updade user from id with PUT
    """
    users = get_users()
    user = get_id(user_id)

    user_data = get_request_data()

    err_check = User.data_check(user_data)
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


@user_bp.route('/users/<string:user_id>', methods=['DELETE'])
def delete_id(user_id):
    """
    Delete user from id with DELETE
    """
    user = get_id(user_id)

    data_manager.delete('user_id', user)
    return jsonify({'user deleted': user['email']}), 200
