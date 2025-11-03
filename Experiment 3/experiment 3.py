from flask import Flask, request, jsonify

app = Flask(__name__)

# Path parameter endpoint
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    # Return product ID in JSON
    return jsonify({'product_id': id})

# Query parameter endpoint
@app.route('/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    # Return category in JSON
    return jsonify({'category': category})

if __name__ == '__main__':
    app.run(debug=True)