from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append({"id": len(users) + 1, **data})
    return jsonify({"message": "User created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
