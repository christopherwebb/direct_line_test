from flask import Flask, request, jsonify


application = Flask(__name__)


# Using POST to handle very large requests
@application.route("/total", methods=['POST'])
def total():
    request_data = request.get_json()

    if not request_data or 'values' not in request_data:
        return "No data of the form {'values': [1, 2, 3]}", 400

    if not isinstance(request_data['values'], list):
        return "'values' should be a list of ints", 400

    try:
        result = sum(int(x) for x in request.get_json()['values'])
    except ValueError:
        return "Bad value, all members of 'values' array should be ints", 400

    return jsonify({'total': result})
