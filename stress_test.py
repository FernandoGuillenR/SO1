from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_coordinates(self):
        cities = ["Lima,Peru", "Buenos Aires,Argentina", "Santiago,Chile"]
        for city in cities:
            self.client.get(f"/coordinates/{city}")
