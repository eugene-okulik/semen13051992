import requests


def all_posts():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    print(response.json())
    print(response.status_code)


all_posts()


def one_post():
    response = requests.get('http://objapi.course.qa-practice.com/object/400')
    print(response.json())
    print(response.status_code)


one_post()


def new_post():
    body = {
        "data" :
                {
                "qcolor": "wblue",
                "ssize": "fsmall"
                },
        "id": 1,
        "name": "crabbit"
    }
    headers = {'User-Agent': 'PostmanRuntime/7.51.1'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    print(response.json())
    print(response.status_code)
    return response.json()['id']


def put_a_post():
    post_id = new_post()
    body = {
        "data":
                {
                "qcdgolor": "wbdglue",
                "sdgsize": "fsmaldgl"
                },
        "id": 1,
        "name": "crabgdgdbit"
    }
    headers = {'User-Agent': 'PostmanRuntime/7.51.1'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    )
    print(response.json())
    print(response.status_code)
    return response.json()['id']


def patch_a_post():
    post_id = put_a_post()
    body = {
        "name": "pelgprtlpgrojnjofklagds"
    }
    headers = {'User-Agent': 'PostmanRuntime/7.51.1'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    )
    print(response.json())
    print(response.status_code)
    return response.json()['id']


def delete_a_post():
    post_id = patch_a_post()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    print(response)
    print(response.status_code)


delete_a_post()
