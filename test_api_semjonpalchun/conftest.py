import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.update_put_object import UpdateObjectPut
from endpoints.update_patch_object import UpdateObjectPatch


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_put_endpoint():
    return UpdateObjectPut()


@pytest.fixture()
def update_object_patch_endpoint():
    return UpdateObjectPatch()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_object_endpoint):
    body = {"data":{"color": "blue","size": "big"},"name": "crabbit"}
    create_object_endpoint.create_new_object(body)
    yield create_object_endpoint.object_id
