import requests

# Base URL
BASE_URL = "http://localhost:5000"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    print("✅ GET /users passed")

def test_create_user():
    data = {"name": "Alice", "email": "alice@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=data)
    assert response.status_code == 201
    print("✅ POST /users passed")

def test_get_invalid_user():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404
    print("✅ GET /users/9999 handled correctly")

if __name__ == "__main__":
    test_get_users()
    test_create_user()
    test_get_invalid_user()
    print("🎯 All automated tests completed successfully!")