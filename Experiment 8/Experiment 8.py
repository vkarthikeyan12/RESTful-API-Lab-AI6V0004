from flask import Flask, jsonify, abort, request

app = Flask(__name__)

# Sample data
users = {
    1: {"name": "Alice"},
    2: {"name": "Bob"}
}

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        abort(400, description="User ID must be an integer")

    if user_id not in users:
        abort(404, description="User not found")

    return jsonify({"id": user_id, "name": users[user_id]["name"]}), 200


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "error": "Bad Request",
        "message": str(error)
    }), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not Found",
        "message": str(error)
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(error)
    }), 500


if __name__ == '__main__':
    app.run(debug=True)
