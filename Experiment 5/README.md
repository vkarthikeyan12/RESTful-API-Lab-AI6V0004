# Experiment 5: REST API with File-Based Storage

## Objective
Persist API data in a JSON file so that data remains available even after server restarts.

## Tools Required
- Python 3.x  
- Flask  
- JSON file for storage  
- cURL   

## Theory
File-based storage allows you to simulate a lightweight database. Using a JSON file, data can be read and written easily, making it ideal for small applications or prototyping REST APIs.

## Procedure

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run the code
```
### **Step2: Test the API**

### Get all books

```
curl -X GET http://localhost:5000/books
```

### Add a new book

```
curl -X POST http://localhost:5000/books -H "Content-Type: application/json" -d "{\"title\":\"Book1\",\"author\":\"Author1\"}"
```

```
Check persistence after restart (look for book.json file)
Stop and restart the Flask server:
```

### Then run GET again:

```
curl -X GET http://localhost:5000/books
```