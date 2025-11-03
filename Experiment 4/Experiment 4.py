from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for items
items = []
current_id = 1

# Create an item
@app.route('/items', methods=['POST'])
def create_item():
    global current_id
    data = request.json
    item = {
        "id": current_id,
        "name": data.get("name", "")
    }
    items.append(item)
    current_id += 1
    return jsonify(item), 201

# Read all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    for item in items:
        if item["id"] == item_id:
            item["name"] = data.get("name", item["name"])
            return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    for item in items:
        if item["id"] == item_id:
            items = [i for i in items if i["id"] != item_id]
            return jsonify({"message": "Item deleted"}), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
