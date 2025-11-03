# Experiment 3: Using URL Parameters and Query Strings

## Objective
Implement endpoints that use URL and query parameters to return dynamic JSON responses.

## Tools Required
- Python 3.x
- Flask
- curl

## Theory
APIs can receive parameters in two main ways:

1. **Path Parameters**  
   - Part of the URL path, e.g., `/products/1`.  
   - Used to identify a specific resource.

2. **Query Parameters**  
   - Added after `?` in the URL, e.g., `/products?category=electronics`.  
   - Used to filter or modify the response

## Procedure

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run the code
```
### **Step2: Test the API**

```commandline
curl -X GET "http://127.0.0.1:5000/products/14"
curl -X GET "http://127.0.0.1:5000/products?category=toys"
```