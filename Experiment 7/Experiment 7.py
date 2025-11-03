from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a sample API key (in real apps, store securely)
VALID_API_KEY = "mysecretapikey123"

# Middleware-like function to check API key
@app.before_request
def check_api_key():
    api_key = request.headers.get("x-api-key")
    if not api_key or api_key != VALID_API_KEY:
        return jsonify({"error": "Unauthorized - Invalid or missing API key"}), 401

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Access granted!", "data": ["item1", "item2", "item3"]})

if __name__ == '__main__':
    app.run(debug=True)
