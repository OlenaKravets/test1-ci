def test_get_users():
    url = "https://reqres.in/api/users?page=1"
    response = requests.get(url)
    assert response.status_code == 200, f"❌ Очікували 200, отримали {response.status_code}"
    data = response.json()
    assert "data" in data, "❌ Відповідь не містить 'data'"

def test_create_user():
    payload = {
        "name": "Olena",
        "job": "QA Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201, f"❌ Очікували 201, отримали {response.status_code}"
    data = response.json()
    assert data["name"] == "Olena", "❌ Ім'я не співпадає"
    assert data["job"] == "QA Engineer", "❌ Робота не співпадає"
