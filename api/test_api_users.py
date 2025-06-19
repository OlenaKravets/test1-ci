import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    print("🔍 GET:", response.status_code, response.text)
    assert response.status_code == 200, f"❌ Очікували 200, отримали {response.status_code}"

def test_create_user():
    payload = {
        "name": "Olena",
        "username": "qa_olena"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    print("📨 POST:", response.status_code, response.text)
    assert response.status_code == 201 or response.status_code == 200, \
        f"❌ Очікували 200 або 201, отримали {response.status_code}"
