# Experiment 1: Introduction to REST and HTTP Methods

## **Aim**
To understand the basic principles of REST architecture and perform CRUD operations using HTTP methods.

## **Objective**
- Learn about REST (Representational State Transfer) architecture.  
- Understand and use HTTP methods: **GET, POST, PUT, DELETE**.  
- Create a simple server and test API endpoints.  

## **Tools Required**
- Python Flask  
- cURL  

## **Theory**
REST (Representational State Transfer) is an architectural style for designing networked applications.  
- **Resources** are data objects (like users, messages, products) accessed via **URIs**.  
- Common HTTP methods:
  | Method | Description                        |
  |--------|------------------------------------|
  | GET    | Retrieve a resource                |
  | POST   | Create a new resource              |
  | PUT    | Update an entire resource          |
  | PATCH  | Partially update a resource        |
  | DELETE | Delete a resource                  |

---

## **Procedure**

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run the code
```
### **Step2: Test the API**

```commandline
curl -X GET http://localhost:5000/hello
curl -X POST http://localhost:5000/hello -H "Content-Type: application/json" -d "{\"name\":\"Karthikeyan\"}"
curl -X PUT http://localhost:5000/hello -H "Content-Type: application/json" -d "{\"name\":\"Karthikeyan\"}"
curl -X DELETE http://localhost:5000/hello
```