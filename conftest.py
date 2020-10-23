import pytest
import requests


# @pytest.fixture(scope="function")
# def error_404():
#     s = requests.Session()
#     s.request(
#        params = "hhttps://jsonplaceholder.typicode.com/posts/gfn,mfg",
#          "https://jsonplaceholder.typicode.com/posts/-1",
#         "https: // jsonplaceholder.typicode.com/posts/10000",
#         "https: // jsonplaceholder.typicode.com/posts/0"
#     )
#     return s

@pytest.fixture
def url():
    return "https://jsonplaceholder.typicode.com/posts"


