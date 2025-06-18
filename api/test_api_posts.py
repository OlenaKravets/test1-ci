import requests

def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    assert response.status_code == 200, f"❌ Очікували 200, отримали {response.status_code}"

    data = response.json()
    assert isinstance(data, list), "❌ Відповідь не є списком"
    assert len(data) > 0, "❌ Список постів порожній"
    assert "title" in data[0], "❌ Поле 'title' відсутнє в першому записі"
