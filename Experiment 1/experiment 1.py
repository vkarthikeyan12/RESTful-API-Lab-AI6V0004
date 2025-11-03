from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def get_hello():
    return jsonify({"message": "GET request received"})

@app.route('/hello', methods=['POST'])
def post_hello():
    data = request.get_json()
    return jsonify({"message": "POST request received", "data": data})

@app.route('/hello', methods=['PUT'])
def put_hello():
    data = request.get_json()
    return jsonify({"message": "PUT request received", "data": data})

@app.route('/hello', methods=['DELETE'])
def delete_hello():
    return jsonify({"message": "DELETE request received"})

if __name__ == '__main__':
    app.run(debug=True)