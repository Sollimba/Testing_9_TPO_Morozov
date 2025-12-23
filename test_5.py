import requests

HEADERS = {"User-Agent": "pytest/reqres-tests"}

def test_get_user_2():
    r = requests.get("https://reqres.in/api/users/2", headers=HEADERS, timeout=10)
    assert r.status_code == 200, f"Unexpected status: {r.status_code}"
    data = r.json().get("data", {})
    assert data.get("id") == 2, "User ID mismatch"
    assert "email" in data and "@" in data["email"], "Email format error"

def test_post_create_user():
    payload = {"name": "test1", "job": "test2"}
    r = requests.post("https://reqres.in/api/users", json=payload, headers=HEADERS, timeout=10)
    assert r.status_code == 201, f"Unexpected status: {r.status_code}"
    j = r.json()
    assert j.get("name") == "test1", "Name mismatch in response"
    assert isinstance(j.get("id"), str), "ID type error"

def test_put_update_user():
    payload = {"name": "test3", "job": "test4"}
    r = requests.put("https://reqres.in/api/users/2", json=payload, headers=HEADERS, timeout=10)
    assert r.status_code == 200, f"Unexpected status: {r.status_code}"
    j = r.json()
    assert j.get("name") == "test3", "Name mismatch in PUT response"
    assert isinstance(j.get("updatedAt"), str), "UpdatedAt type error"