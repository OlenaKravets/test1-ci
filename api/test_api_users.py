import requests

BASE_URL = "https://reqres.in/api"

def test_get_users():
    url = f"{BASE_URL}/users?page=1"
    response = requests.get(url)
    assert response.status_code == 200

def test_create_user():
    payload = {
        "name": "Olena",
        "job": "QA Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
