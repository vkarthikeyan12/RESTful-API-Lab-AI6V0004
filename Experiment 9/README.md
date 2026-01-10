# Experiment 9: Testing APIs using Postman Collection (via Python & curl)

## 🎯 Objective
Automate API testing using scripts instead of Hoppscotch.

---

## 🧰 Tools Required
- Testing URL
- Hoppscotch
- ---

## 🧠 Theory
Hoppscotch automates API testing using collections, but the same concept can be achieved with Python scripts or `curl` commands.  
Each test verifies response codes, data structure, or content.  
This helps ensure that APIs work as expected under automation.

## Testing URL
```
https://jsonplaceholder.typicode.com/comments
```
## Procedure

### **Step 1: Identify URL**

**Choose the correct URL**

1. Click to add PRE request script

```

// Set an environment variable
pw.env.set("variable", "value");

// Set timestamp variable
const currentTime = Date.now();
pw.env.set("timestamp", currentTime.toString());

// Set random number variable
const min = 1
const max = 1000
const randomArbitrary = Math.random() * (max - min) + min
pw.env.set("randomNumber", randomArbitrary.toString());
```

2. Check for response
```
{
  "id": 501
}
```

3. Click to add Post request script
```


// Set an environment variable
pw.env.set("variable", "value");

// Check status code is 200
pw.test("Status code is 200", ()=> {
    pw.expect(pw.response.status).toBe(200);
});

// Check JSON response property
pw.test("Check JSON response property", ()=> {
    pw.expect(pw.response.body.method).toBe("GET");
});

// Check status code is 2xx
pw.test("Status code is 2xx", ()=> {
    pw.expect(pw.response.status).toBeLevel2xx();
});

// Check status code is 3xx
pw.test("Status code is 3xx", ()=> {
    pw.expect(pw.response.status).toBeLevel3xx();
});

// Check status code is 4xx
pw.test("Status code is 4xx", ()=> {
    pw.expect(pw.response.status).toBeLevel4xx();
});

// Check status code is 5xx
pw.test("Status code is 5xx", ()=> {
    pw.expect(pw.response.status).toBeLevel5xx();
});
```

4. Check for response
```
{
  "id": 501
}
```

