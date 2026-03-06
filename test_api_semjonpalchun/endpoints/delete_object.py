import requests
import allure
from semen13051992.test_api_semjonpalchun.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    object_id = None

    @allure.feature("test_api")
    @allure.story("test_delete_object")
    @allure.title("Удаление объекта")
    @allure.step('Delete object')
    def delete_object(self, object_id):
        self.object_id = object_id
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response
