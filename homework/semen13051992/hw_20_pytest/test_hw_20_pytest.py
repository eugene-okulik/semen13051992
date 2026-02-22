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


@pytest.mark.critical
def test_all_object(hello, tests):
    response = requests.get('http://objapi.course.qa-practice.com/object')
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200


@pytest.mark.medium
def test_one_post(new_object, tests):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object}')
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert response.json()['id'] == new_object


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


def test_put_a_object(new_object, tests):
    body = {
        "data":
        {
            "color": "wbdglue",
            "size": "fsmaldgl"
        },
        "name": "crabgd"
    }
    headers = {'User-Agent': 'PostmanRuntime/7.51.1'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object}',
        json=body,
        headers=headers
    )
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert response.json()['id'] == str(new_object)


def test_patch_a_object(new_object, tests):
    body = {
        "name": "pelgprtlpgr"
    }
    headers = {'User-Agent': 'PostmanRuntime/7.51.1'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object}',
        json=body,
        headers=headers
    )
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert response.json()['id'] == new_object


def test_delete_a_object(new_object, tests):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object}')
    print(response)
    print(response.status_code)
    assert response.status_code == 200


@pytest.mark.parametrize(
    'color, size, name',
    [
        ("red", "blue", "gold"),
        ("average", "big", "little"),
        ("acrylic", "oil", "painting")
    ])
def test_new_object(color, size, name):
    body = {
        "data":
        {
            "color": color,
            "size": size
        },
        "name": name
    }
    headers = {'User-Agent': 'PostmanRuntime/7.51.1'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200
    object_id = response.json()['id']
    print(object_id)
    print('deleting the post')
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200
