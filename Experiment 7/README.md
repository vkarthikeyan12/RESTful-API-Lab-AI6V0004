# 🧪 Experiment 7: Authentication using API Keys

## 🎯 Objective
Secure APIs using API keys to restrict access only to authorized clients.

---

## 🧰 Tools Required
- Python  
- Flask  
- cURL

---

## 🧠 Theory
An **API key** is a unique identifier used to authenticate a client or application accessing an API.  
It acts like a password — the server verifies the key before processing requests.  

**Authentication** ensures the identity of the user or system.  
**Authorization** determines what an authenticated user is allowed to do.

## Procedure

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run the code
```
### **Step2: Test the API**

✅ Authorized Request

```
curl -X GET http://localhost:5000/data -H "x-api-key: mysecretapikey123"
```

❌ Unauthorized Request (No API Key)

```
curl -X GET http://localhost:5000/data
```

❌ Invalid API Key

```
curl -X GET http://localhost:5000/data -H "x-api-key: wrongkey"
```