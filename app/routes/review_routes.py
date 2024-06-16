#!/usr/bin/python3
"""
python module for review routes
"""
from flask import Blueprint, jsonify
from app.persistence.data_manager import DataManager


review_bp = Blueprint('reviews', __name__)
data_manager_review = DataManager('storage/review.json')
data_manager_place = DataManager('storage/place.json')
data_manager_user = DataManager('storage/user.json')


@review_bp.route('/users/<string:user_id>/reviews', methods=['GET'])
def get_by_user_id(user_id):
    """
    Retrieve review from user_id with GET
    """
    reviews = data_manager_review.get()
    users = data_manager_user.get()

    if reviews is False:
        return jsonify({'Error': 'reviews not found'}), 404

    if users is False:
        return jsonify({'Error': 'users not found'}), 404

    for user in users:
        if user['user_id'] == user_id:
            user_reviews = [
                review for review in reviews if review['user_id'] == user_id]
            return jsonify(user_reviews), 200


@review_bp.route('/places/<string:place_id>/reviews', methods=['GET'])
def get_by_place_id(place_id):
    """
    Retrieve review from place_id with GET
    """
    reviews = data_manager_review.get()
    places = data_manager_place.get()

    if reviews is False:
        return jsonify({'Error': 'reviews not found'}), 404

    if places is False:
        return jsonify({'Error': 'places not found'}), 404

    for review in reviews:
        if review['place_id'] == place_id:
            place_reviews = [
                review for review in reviews if review['place_id'] == place_id]
            return jsonify(place_reviews), 200


@review_bp.route('/reviews/<string:review_id>', methods=['GET'])
def get_review_id(review_id):
    """
    Retrieve review from review_id with GET
    """
    reviews = data_manager_review.get()

    if reviews is False:
        return jsonify({'Error': 'reviews not found'}), 404

    for review in reviews:
        if review['review_id'] == review_id:
            return jsonify(review), 200
