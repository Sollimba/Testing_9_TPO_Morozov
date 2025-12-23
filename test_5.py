import requests

BASE_URL = "https://reqres.in/api"


def test_get_user_2():
    response = requests.get(f"{BASE_URL}/users/2", timeout=10)

    assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    body = response.json()
    assert "data" in body, "Missing 'data' field in response"

    user = body["data"]
    assert user["id"] == 2, "User ID mismatch"
    assert "@" in user["email"], "Invalid email format"


def test_post_create_user():
    payload = {
        "name": "test1",
        "job": "test2"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201, f"Unexpected status: {response.status_code}"

    body = response.json()
    assert body["name"] == payload["name"], "Name mismatch"
    assert "id" in body, "Missing id in response"
    assert isinstance(body["id"], str), "id is not a string"


def test_put_update_user():
    payload = {
        "name": "test3",
        "job": "test4"
    }

    response = requests.put(
        f"{BASE_URL}/users/2",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    body = response.json()
    assert body["name"] == payload["name"], "Name mismatch"
    assert "updatedAt" in body, "Missing updatedAt field"
