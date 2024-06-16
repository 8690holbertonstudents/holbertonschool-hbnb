#!/usr/bin/python3
"""
python module for
"""
from flask import request, jsonify


def get_request_data():
    """
    Get data from request phrase
    """
    try:
        request_data = request.get_json()
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

    if not isinstance(request_data, dict):
        return jsonify({'Error': 'Data are not JSON object'}), 400

    return request_data
