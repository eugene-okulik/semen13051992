import pytest

TEST_DATA = [
    {"data": {"color": "blue", "size": "big"}, "name": "crabbit"},
    {"data": {"color": "wsfsd", "size": "fsdvsd"}, "name": "qwre"},
    {"data": {"color": "okcsdl", "size": "qljlf"}, "name": "pwjcd"}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(data['name'])
    create_object_endpoint.check_response_data_is_correct(data['data'])


def test_put_a_object(update_object_put_endpoint, object_id):
    data = {"data": {"color": "sdfsdf", "size": "biwffg"}, "name": "ervvfr"}
    update_object_put_endpoint.update_object_put(object_id, data)
    update_object_put_endpoint.check_that_status_is_200()
    update_object_put_endpoint.check_response_name_is_correct(data['name'])
    update_object_put_endpoint.check_response_data_is_correct(data['data'])


def test_patch_a_object(update_object_patch_endpoint, object_id):
    data = {"name": "sklqld"}
    update_object_patch_endpoint.update_object_patch(object_id, data)
    update_object_patch_endpoint.check_that_status_is_200()
    update_object_patch_endpoint.check_response_name_is_correct(data['name'])


def test_delete_a_object(object_id, delete_object_endpoint):
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_that_status_is_200()


def test_get_a_object(get_object_endpoint, object_id):
    get_object_endpoint.get_object(object_id)
    get_object_endpoint.check_that_status_is_200()


def test_get_all_objects(get_object_endpoint):
    get_object_endpoint.get_all_objects()
    get_object_endpoint.check_that_status_is_200()
