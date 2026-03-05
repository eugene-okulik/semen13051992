import requests
import allure

from semen13051992.test_api_semjonpalchun.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None

    @allure.feature("test_api")
    @allure.story("test_new_object")
    @allure.title("Создание объекта")
    @allure.step('Create new object')
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
