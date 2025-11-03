# Experiment 4: Performing CRUD Operations

## Objective
Implement Create, Read, Update, and Delete (CRUD) operations on an in-memory list using a RESTful API.

## Tools Required
- Python 3.x  
- Flask  
- cURL

## Theory
CRUD operations form the backbone of RESTful services:  
- **Create** → Add new resources (POST)  
- **Read** → Retrieve resources (GET)  
- **Update** → Modify existing resources (PUT/PATCH)  
- **Delete** → Remove resources (DELETE)

## Procedure

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run the code
```
### **Step2: Test the API**

1. Create an item (POST)

```
curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d "{\"name\":\"Item1\"}"
```

2. Read all items (GET)

```
curl -X GET http://localhost:5000/items
```

3. Update an item (PUT)


```
curl -X PUT http://localhost:5000/items/1 -H "Content-Type: application/json" -d "{\"name\":\"UpdatedItem1\"}"
```

4. Delete an item (DELETE)

```
curl -X DELETE http://localhost:5000/items/1
```