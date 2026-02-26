import requests
import pytest


@pytest.fixture()
def new_object():
    body = {
        "data":
            {
                "color": "blue",
                "size": "big"
            },
        "name": "crabbit"
    }
    headers = {'User-Agent': 'PostmanRuntime/7.51.1'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    print(object_id)
    yield object_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object}')


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
