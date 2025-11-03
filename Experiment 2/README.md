# Experiment 2: Building a Simple REST API

## Objective
Design a REST API that returns JSON data for a list of users.

## Tools Required
- Flask (Python) 

## Theory
A **REST API (Representational State Transfer Application Programming Interface)** allows communication between client and server over HTTP.  
REST APIs commonly use **JSON (JavaScript Object Notation)** as the data format, which is lightweight, easy to read, and easy to parse.

## Procedure

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run the code
```
### **Step2: Test the API**

```commandline
curl -X GET http://127.0.0.1:5000/users
curl -X GET http://127.0.0.1:5000/users/1
```