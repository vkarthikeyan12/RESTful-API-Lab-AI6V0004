# 🧪 Experiment 8: Error Handling and Status Codes

## 🎯 Objective
Implement structured error handling with proper HTTP status codes in a REST API.

---

## 🧰 Tools Required
- Python 3.x  
- Flask Framework  
- cURL  

---

## 📘 Theory
HTTP status codes are standardized responses that indicate the result of a client’s request to a server. They help developers and clients understand whether a request succeeded or failed.

### Common Categories:
- **2xx (Success)** – The request was successfully processed.  
  Example: `200 OK`, `201 Created`
- **4xx (Client Error)** – The client sent a bad request.  
  Example: `400 Bad Request`, `404 Not Found`, `401 Unauthorized`
- **5xx (Server Error)** – The server failed to process a valid request.  
  Example: `500 Internal Server Error`, `503 Service Unavailable`

## Procedure

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run the code
```
### **Step2: Test the API**

✅ 1. Valid Request

```
curl -X GET http://localhost:5000/users/1
```


❌ 2. User Not Found

```
curl -X GET http://localhost:5000/users/99
```


❌ 3. Non-Integer User ID
```
curl -X GET http://localhost:5000/users/abc
```