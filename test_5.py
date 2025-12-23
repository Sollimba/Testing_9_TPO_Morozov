import pytest
import requests
import responses

@responses.activate
def test_get_user_2():
    # Мокируем GET-запрос
    responses.add(
        responses.GET,
        "https://reqres.in/api/users/2",
        json={"data": {"id": 2, "email": "test@example.com"}},
        status=200
    )

    r = requests.get("https://reqres.in/api/users/2")
    assert r.status_code == 200
    data = r.json()["data"]
    assert data["id"] == 2
    assert "@" in data["email"]

@responses.activate
def test_post_create_user():
    # Мокируем POST-запрос
    responses.add(
        responses.POST,
        "https://reqres.in/api/users",
        json={"id": "123", "name": "test1", "job": "test2"},
        status=201
    )

    payload = {"name": "test1", "job": "test2"}
    r = requests.post("https://reqres.in/api/users", json=payload)
    assert r.status_code == 201
    j = r.json()
    assert j["name"] == "test1"
    assert j["job"] == "test2"

@responses.activate
def test_put_update_user():
    # Мокируем PUT-запрос
    responses.add(
        responses.PUT,
        "https://reqres.in/api/users/2",
        json={"name": "test3", "job": "test4", "updatedAt": "2025-12-23T00:00:00Z"},
        status=200
    )

    payload = {"name": "test3", "job": "test4"}
    r = requests.put("https://reqres.in/api/users/2", json=payload)
    assert r.status_code == 200
    j = r.json()
    assert j["name"] == "test3"
    assert j["job"] == "test4"
    assert "updatedAt" in j