import requests
import pytest


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def tests():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def url():
    url = 'http://memesapi.course.qa-practice.com'
    return url


def test_authorize(url):
    response = requests.post(
        f'{url}/authorize',
                json={'name': 'qwerty'}
        )
    token = response.json()['token']
    assert response.status_code == 200

def test_authorize_token(url, token):
    response = requests.post(
        f'{url}/authorize/{token}',
                json={'name': 'qwerty'}
        )
    assert response.json()['token']
    assert response.status_code == 200

#def test_authorize(token):
    if token == authorize_token():
        token = token
    else:
        authorize()

