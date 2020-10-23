import requests
import pytest


def test_return_specific_user():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200, "handle must return 200 OK"


def test_post_specific_user():
    response = requests.post("https://reqres.in/api/users/2")
    assert response.status_code == 201, "must return 201 created"


def test_add_new_user_valid():
    response = requests.request(
        method="post",
        url="https://reqres.in/api/users",
        json={"name": "bob", "job": "qa engineer"}
    )
    assert response.status_code == 201, "must return 201 Created code "


def test_add_new_user_correct_credentials():
    response = requests.post(
        url="https://reqres.in/api/register",
        json={"email": "eve.holt@reqres.in", "password": "pistol"}
    )
    assert response.status_code == 200, "must return 200 OK code"


def test_add_new_user_wrong_credentials():
    response = requests.request(
        method="post",
        url="https://reqres.in/api/register",
        json={"name": "bob", "password": "123"}
    )
    assert response.status_code == 400, "must return 404 error - bad request"


def test_return_non_existing_user():
    response = requests.get("https://reqres.in/api//unkown/9999")
    assert response.status_code == 404, "must return 404 error - not found"
