import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'User-Agent': 'PostmanRuntime/7.51.1'}


    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200


    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400


    @allure.step('Check that title is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name


    @allure.step('Check that id is the same as sent')
    def check_response_data_is_correct(self, data):
        assert self.json['data'] == data
