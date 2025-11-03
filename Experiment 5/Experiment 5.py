from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
FILE = 'books.json'

# Ensure file exists
if not os.path.exists(FILE):
    with open(FILE, 'w') as f:
        json.dump([], f)

def read_books():
    with open(FILE, 'r') as f:
        return json.load(f)

def write_books(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(read_books())

@app.route('/books', methods=['POST'])
def add_book():
    books = read_books()
    book = request.json
    books.append(book)
    write_books(books)
    return jsonify(book), 201

if __name__ == '__main__':
    app.run(debug=True)
