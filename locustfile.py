import json
import time

from locust import HttpUser, between, task, TaskSet
from django.views.decorators.csrf import csrf_exempt, csrf_protect


class MyTasks(TaskSet):
    @task(1)
    def product_list(self):
        self.client.get('/myapp/product_list')
    @task(3)
    def product_Details(self):
        self.client.get('/myapp/product_details/1')

    # @csrf_protect
    @task(2)
    def product_Save(self):
        self.client.post('/myapp/product_save', {"id":4, "Name": "mobile", "Price": 3000,"Code":"102"} )



class ApiUser(HttpUser):
    wait_time = between(2, 5)

    @csrf_exempt
    # @csrf_protect
    def on_start(self):
        self.client.post("/api/token/", json={"username": "mina", "password": "mina123456"})

    tasks = {MyTasks}



# locust --host=http://127.0.0.1:8000 -f locustfile.py