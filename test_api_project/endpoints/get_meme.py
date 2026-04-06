import requests
import allure

from semen13051992.test_api_semjonpalchun.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    object_id = None

    @allure.feature("test_api")
    @allure.story("test_get_object")
    @allure.title("Получение объекта")
    @allure.step('Get objects')
    def get_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        return self.response

    @allure.feature("test_api")
    @allure.story("test_get_all_objects")
    @allure.title("Получение объектов")
    @allure.step('Get all objects')
    def get_all_objects(self):
        self.response = requests.get(f'{self.url}')
        return self.response
