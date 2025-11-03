from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Home route - renders HTML template
@app.route('/')
def home():
    return render_template('index.html')

# Simple API route
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "API is live!",
        "users": ["Alice", "Bob", "Charlie"]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
