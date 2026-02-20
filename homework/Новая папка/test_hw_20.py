import requests
import pytest


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def test():
    print("before test")
    yield
    print("after test")


@pytest.mark.critical
def test_all_object(hello, test):
    response = requests.get('http://objapi.course.qa-practice.com/object')
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200


@pytest.mark.medium
def test_one_post(test):
    response = requests.get('http://objapi.course.qa-practice.com/object/1')
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert response.json()['id'] == 1


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
    print('deleting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{object_id}')


def test_put_a_object(new_object, test):
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


def test_patch_a_object(new_object, test):
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

def test_delete_a_object(new_object, test):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object}')
    print(response)
    print(response.status_code)
    assert response.status_code == 200


'''
@pytest.mark.parametrize('color', ["red", "blue", "gold"],
                        'size',["average", "big", "little"],
                         'name',["acrylic", "oil painting"])


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
    object_id = response.json()['id']
    print(object_id)
    print('deleting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{object_id}')
'''
