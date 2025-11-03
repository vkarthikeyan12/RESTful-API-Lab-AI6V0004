# Experiment 9: Testing APIs using Postman Collection (via Python & curl)

## 🎯 Objective
Automate API testing using scripts instead of Postman.

---

## 🧰 Tools Required
- Python 3  
- `requests` library 
- curl command-line tool

---

## 🧠 Theory
Postman automates API testing using collections, but the same concept can be achieved with Python scripts or `curl` commands.  
Each test verifies response codes, data structure, or content.  
This helps ensure that APIs work as expected under automation.

## Procedure

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run the API TEST
Run Experiment 9.py
```
### **Step2: Test the API**

1. GET all users
```
curl -X GET http://localhost:5000/users
```

2. POST new user
```
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d "{\"name\":\"Alice\",\"email\":\"alice@example.com\"}"
```

3. GET specific user
```
curl -X GET http://localhost:5000/users/1
```

4. Invalid user test (expect 404)
```
curl -X GET http://localhost:5000/users/9999
```

5. Check status code only
```
curl -o /dev/null -s -w "%{http_code}\n" http://localhost:5000/users
```