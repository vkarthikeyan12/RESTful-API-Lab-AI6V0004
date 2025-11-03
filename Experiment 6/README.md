# Experiment 5: REST API with File-Based Storage

## Objective
Integrate SQLite database with a RESTful API to perform CRUD operations.

## Tools Required
- Python 3.x  
- Flask  
- JSON file for storage  
- cURL

## Theory
Databases are used to store structured or unstructured data for APIs.
**SQLite**: Lightweight relational database stored in a single file.
**SQLAlchemy** (ORM): Allows interaction with the database using Python objects instead of raw SQL queries.

## Procedure

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run the code
```
### **Step2: Test the API**

1. Create a user (POST)

```
  curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d "{\"name\":\"Alice\",\"email\":\"alice@example.com\"}"
```

2. Get all users (GET)

```
curl -X GET http://localhost:5000/users
```

3. Get user by ID (GET)

```
curl -X GET http://localhost:5000/users/1
```

4. Update user by ID (PUT)

```
curl -X PUT http://localhost:5000/users/1 -H "Content-Type: application/json" -d "{\"name\":\"Alice Smith\",\"email\":\"alice.smith@example.com\"}"
```

5. Delete user by ID (DELETE)

```
curl -X DELETE http://localhost:5000/users/1
```