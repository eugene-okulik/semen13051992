import requests
import pytest
import allure


@allure.feature("test_api")
@allure.story("test_all_object")
@allure.title("Получение всех объектов")
@pytest.mark.critical
def test_all_object(hello, tests):
    with allure.step('Run request to get a object'):
        response = requests.get('http://objapi.course.qa-practice.com/object')
    with allure.step(f'All object. Check response code is 200'):
        assert response.status_code == 200


@allure.feature("test_api")
@allure.story("test_one_object")
@allure.title("Получение одного объекта")
@pytest.mark.medium
def test_one_object(new_object, tests):
    with allure.step('Run request to get a object'):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_object}')
    with allure.step('Check response code is 200'):
        assert response.status_code == 200
    with allure.step(f'The object id is equal to the id {new_object}'):
        assert response.json()['id'] == new_object


@allure.feature("test_api")
@allure.story("test_put_object")
@allure.title("Обновление объекта")
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
    with allure.step('Run request to put a object'):
        response = requests.put(
            f'http://objapi.course.qa-practice.com/object/{new_object}',
            json=body,
            headers=headers
        )
    with allure.step('Check response code is 200'):
        assert response.status_code == 200
    with allure.step(f'The object id is equal to the id {new_object}'):
        assert response.json()['id'] == str(new_object)


@allure.feature("test_api")
@allure.story("test_patch_object")
@allure.title("Обновление имени объекта")
def test_patch_a_object(new_object, tests):
    body = {
        "name": "pelgprtlpgr"
    }
    headers = {'User-Agent': 'PostmanRuntime/7.51.1'}
    with allure.step('Run request to patch a object'):
        response = requests.patch(
            f'http://objapi.course.qa-practice.com/object/{new_object}',
            json=body,
            headers=headers
        )
    with allure.step('Check response code is 200'):
        assert response.status_code == 200
    with allure.step(f'The object id is equal to the id {new_object}'):
        assert response.json()['id'] == new_object


@allure.feature("test_api")
@allure.story("test_delete_object")
@allure.title("Удаление объекта")
def test_delete_a_object(new_object, tests):
    with allure.step('Run request to delete a object'):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object}')
    with allure.step('Check response code is 200'):
        assert response.status_code == 200


@allure.feature("test_api")
@allure.story("test_new_object")
@allure.title("Создание трех объектов")
@pytest.mark.parametrize(
    'color, size, name',
    [
        ("red", "blue", "gold"),
        ("average", "big", "little"),
        ("acrylicq", "oil", "painting")
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
    with allure.step('Run request to post a object'):
        response = requests.post(
            'http://objapi.course.qa-practice.com/object',
            json=body,
            headers=headers
        )
    with allure.step('Check response code is 200'):
        assert response.status_code == 200
    with allure.step('Finding the object id'):
        object_id = response.json()['id']
    with allure.step('Run request to delete a object'):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    with allure.step('Check response code is 200'):
        assert response.status_code == 200
