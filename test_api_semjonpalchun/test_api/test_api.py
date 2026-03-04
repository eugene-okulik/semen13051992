import pytest
from semen13051992.test_api_semjonpalchun.conftest import create_object_endpoint
from semen13051992.test_api_semjonpalchun.conftest import delete_object_endpoint
from semen13051992.test_api_semjonpalchun.conftest import update_object_put_endpoint
from semen13051992.test_api_semjonpalchun.conftest import update_object_patch_endpoint

TEST_DATA = [
    {"data": {"color": "blue", "size": "big"}, "name": "crabbit"},
    {"data": {"color": "wsfsd", "size": "fsdvsd"}, "name": "qwre"}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(data['name'])
    create_object_endpoint.check_response_data_is_correct(data['data'])


@pytest.mark.parametrize('data', TEST_DATA)
def test_put_a_object(create_object_endpoint, update_object_put_endpoint, delete_object_endpoint, object_id, data):
    create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_that_status_is_200()
    data = {"data": {"color": "sdfsdf", "size": "biwffg"}, "name": "ervvfr"}
    update_object_put_endpoint.update_object_put(object_id, data)
    update_object_put_endpoint.check_that_status_is_200()
    # update_object_put_endpoint.check_response_name_is_correct(data['name'])
    # update_object_put_endpoint.check_response_data_is_correct(data['data'])
    # delete_object_endpoint.delete_object(object_id)


@pytest.mark.parametrize('data', TEST_DATA)
def test_patch_a_object(create_object_endpoint, update_object_patch_endpoint, delete_object_endpoint, object_id, data):
    create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_that_status_is_200()
    data = {"name": "sklqld"}
    update_object_patch_endpoint.update_object_patch(object_id, data)
    update_object_patch_endpoint.check_that_status_is_200()
    # update_object_patch_endpoint.check_response_name_is_correct(data['name'])
    # delete_object_endpoint.delete_object(object_id)


@pytest.mark.parametrize('data', TEST_DATA)
def test_delete_a_object(create_object_endpoint, delete_object_endpoint, object_id, data):
    create_object_endpoint.create_new_object(data)
    create_object_endpoint.check_that_status_is_200()
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_that_status_is_200()
