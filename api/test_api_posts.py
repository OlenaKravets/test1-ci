import requests

def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("📰 POSTS:", response.status_code)
    assert response.status_code == 200
