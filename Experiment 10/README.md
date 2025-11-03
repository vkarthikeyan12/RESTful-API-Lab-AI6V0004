# Objective

To host and test a RESTful API locally and then test it

## Tools Required

Python 3
Flask
HTML Template


## Theory

A REST API allows data exchange between client and server using HTTP methods.
Deployment makes the API accessible publicly via the internet, but before deployment, testing locally ensures everything runs as expected.

Local Environment: Runs on localhost, used for development and testing.

Production Environment: Runs on a cloud server, accessible globally.

## Procedure

### **Step 1: Create a Simple Server**

**Python Flask Example:**
```
Run Experiment 10.py
```
### **Step2: Test the API**

```
curl http://127.0.0.1:5000/api/data
```