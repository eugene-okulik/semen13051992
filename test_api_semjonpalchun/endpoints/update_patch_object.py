import requests
import allure

from semen13051992.test_api_semjonpalchun.endpoints.endpoint import Endpoint


class UpdateObjectPatch(Endpoint):

    @allure.feature("test_api")
    @allure.story("test_patch_object")
    @allure.title("Обновление имени объекта")
    @allure.step('Update a object patch')
    def update_object_patch(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
