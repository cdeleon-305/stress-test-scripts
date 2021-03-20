import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(3)
    def hello_world(self):
        self.client.get("/beach")
        self.client.get("/clubandocho")
        self.client.get("/blah")

        

    def on_start(self):
        self.client.get("/cecconis")