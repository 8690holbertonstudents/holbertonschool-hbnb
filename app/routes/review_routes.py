#!/usr/bin/python3
"""
python module for review routes
"""
from flask import Blueprint, jsonify, request, abort
from app.models.review import review
from app.persistence.data_manager import DataManager


review_bp = Blueprint('reviews', __name__)
data_manager = DataManager('app/storage/review.json')


def common_check(review_data):
    """
    Common check for POST and PUT
    """
    if not review_data:
        return jsonify({'Error': 'Bad request, no data'}), 400

    if not isinstance(review_data, dict):
        return jsonify({'Error': 'review is not JSON object'}), 400

    if 'comment' not in review_data:
        return jsonify({'Error': 'review must have a comment'}), 400

    if 'rating' not in review_data:
        return jsonify({'Error': 'review must have a rating'}), 400

    if not isinstance(review_data['comment'], str):
        return jsonify({'Error': 'review comment is not a string'}), 400

    if not isinstance(review_data['rating'], int) and review_data['rating'] not in range(1, 6):
        return jsonify({'Error': 'rating must be an integer between 1 and 5'}), 400

    if len(review_data['comment']) == 0:
        return jsonify({'Error': 'review comment cannot be empty'}), 400

    return None


def get_review_data():
    """
    Get review data from request
    """
    try:
        review_data = request.get_json()
    except:
        return jsonify({'Error': 'Bad JSON object'}), 400

    return review_data


@review_bp.route('/reviews', methods=['GET'])
def get():
    """
    Retrieve reviews list with GET
    """
    reviews = data_manager.get()

    if reviews is None:
        reviews = []

    if reviews is False:
        return jsonify({'Error': 'reviews not found'}), 404

    if request.method == 'GET':
        return jsonify(reviews), 200

    if request.method == 'POST' or request.method == 'PUT':
        return reviews


@review_bp.route('/reviews', methods=['POST'])
def post():
    """
    Add a new review to reviews list with POST
    """
    reviews = get()

    review_data = get_review_data()

    err_check = common_check(review_data)
    if err_check:
        return err_check

    for item in reviews:
        if item['comment'] == review_data['comment']:
            return jsonify({'Error': 'review comment already exist'}), 409

    comment = review_data.get('comment')
    new_review = review(comment)
    if not new_review:
        return jsonify({'Error': 'unable create new review'}), 400

    new_review.__dict__['review_id'] = new_review.__dict__.pop('id')
    if data_manager.save(new_review.__dict__) is False:
        return jsonify({'Error': 'bad json file'}), 409
    return jsonify({'review added': comment}), 200


@review_bp.route('/reviews/<string:review_id>', methods=['GET'])
def get_id(review_id):
    """
    Retrieve review from id with GET
    """
    review = data_manager.get_id(review_id)
    if review is False:
        return abort(404)

    if request.method == 'GET':
        return jsonify(review), 200

    if request.method == 'PUT' or request.method == 'DELETE':
        return review


@review_bp.route('/reviews/<string:review_id>', methods=['PUT'])
def put_id(review_id):
    """
    Updade review from id with PUT
    """
    reviews = get()
    review = get_id(review_id)

    review_data = get_review_data()

    err_check = common_check(review_data)
    if err_check:
        return err_check

    for item in reviews:
        if item['comment'] == review_data['comment']:
            return jsonify({'Error': 'review comment already exist'}), 409

    review['comment'] = review_data['comment']
    data_manager.update('review_id', review)
    return jsonify({'review updated': review['comment']}), 200


@review_bp.route('/reviews/<string:review_id>', methods=['DELETE'])
def delete_id(review_id):
    """
    Delete review from id with DELETE
    """
    review = get_id(review_id)

    data_manager.delete('review_id', review)
    return jsonify({'review deleted': review['comment']}), 200


@review_bp.app_errorhandler(404)
def not_found(error):
    """
    Handle err 404 for undefined routes
    """
    return jsonify({'Error': 'Bad url'}), 404
