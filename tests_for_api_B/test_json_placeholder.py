import requests
import pytest


def test_return_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200, "handle must return 200"


@pytest.mark.parametrize("handle", ["gfn,mfg", -1, 10000, 0])
def test_verify_code404(url, handle):
    url_final = f"{url}/{handle}"
    response = requests.request("get", url_final)
    assert response.status_code == 404, "should return error 404 on invalid handle"


def test_verify_user_id_1():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert data["id"] == 1


def test_verify_status_for_post():
    response = requests.post("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 404, "for post command should return 404 code"


def test_verify_user_amount():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert len(data) == 10


def test_verify_user_by_id2():
    response = requests.get("https://jsonplaceholder.typicode.com/users/2")
    data = response.json()
    assert data["id"] == 2
    assert data["username"] == "Antonette"
    assert data["website"] == "anastasia.net"


def test_verify_all_comments_for_post_id1():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
    assert response.status_code == 200, "handle must return 200"
