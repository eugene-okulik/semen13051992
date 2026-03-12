from locust import task, HttpUser


class MemeUser(HttpUser):

    def on_start(self):
        body = {
            "data":
                {
                    "color": "blue",
                    "size": "big"
                },
            "name": "crabbit"
        }
        object_id = self.client.post(
            '/object',
            json=body,
            headers={'User-Agent': 'PostmanRuntime/7.51.1'}
        )
        self.id = object_id.json()['id']

    @task(1)
    def get_one_object(self):
        self.client.get(
            f'/object/{self.id}',
            headers={'User-Agent': 'PostmanRuntime/7.51.1'}
        )

    @task(1)
    def get_all_object(self):
        self.client.get(
            '/object',
            headers={'User-Agent': 'PostmanRuntime/7.51.1'}
        )

    @task(1)
    def get_put_object(self):
        body = {
            "data":
                {
                    "color": "egdfg",
                    "size": "dgdge"
                },
            "name": "dgdfhg"
        }
        self.client.put(
            f'/object/{self.id}',
            json=body,
            headers={'User-Agent': 'PostmanRuntime/7.51.1'}
        )

    @task(1)
    def get_patch_object(self):
        body = {
            "name": "egfdgt"
        }
        self.client.patch(
            f'/object/{self.id}',
            json=body,
            headers={'User-Agent': 'PostmanRuntime/7.51.1'}
        )

    @task(1)
    def get_delete_object(self):
        self.client.delete(
            f'/object/{self.id}',
            headers={'User-Agent': 'PostmanRuntime/7.51.1'}
        )
