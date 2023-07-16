import random
import uuid
import time
import json
import threading
from faker import Faker
from stream import _stream
faker = Faker()


class GenerateFakeData:
    
    def __init__(self):
        self.d = _stream()
        self.users_list = []
        self.sites_list = []
        self.metrics_list = []
        self.users_id = []
        self.sites_id = []

    def fake_user(self):
        user_id = str(uuid.uuid4())
        first_name = faker.first_name()
        last_name = faker.last_name()
        address = faker.address()
        email = faker.email()
        phone_number = faker.phone_number()
        user = {}
        data = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "email": email,
            "phone_number": phone_number
        }
        return data

    def fake_site(self):
        site_id = str(uuid.uuid4())
        url = faker.url()
        user_id = random.choice(self.users_id)
        user = {}
        data = {
            "site_id": site_id,
            "url": url,
            "user_id": user_id
        }
        return data

    def fake_metrics(self, site_id):
        event_uuid = str(uuid.uuid4())
        event_time = int(time.time())
        metrics = {}
        # Add optional metrics fields with a 50% chance for each field
        if random.random() < 0.5:
            metrics["storage_gb"] = random.randint(1, 100)
        if random.random() < 0.5:
            metrics["disc_cache"] = random.randint(1, 100)
        if random.random() < 0.5:
            metrics["disc_a_gb"] = random.randint(1, 100)
        if random.random() < 0.5:
            metrics["disc_b_gb"] = random.randint(1, 100)
        if random.random() < 0.5:
            metrics["cpu_percent"] = random.randint(1, 100)
        if random.random() < 0.5:
            metrics["cpu_tic"] = random.randint(1, 100)
        data = {
            "event_uuid": event_uuid,
            "event_time": event_time,
            "identifier": {
                "site_id": site_id
            },
            "metrics": metrics
        }
        return data

    def generate_fake_users(self):
        for _ in range(100):
            fake_user = self.fake_user()
            self.users_list.append(fake_user)
            self.users_id.append(fake_user['user_id'])

    def generate_fake_sites(self):
        for _ in range(500):
            fake_site = self.fake_site()
            self.sites_list.append(fake_site)
            self.sites_id.append(fake_site['site_id'])

    def generate_fake_metrics(self,format):

        while True:
            for site_id in self.sites_id:
                fake_metrics = self.fake_metrics(site_id)
                self.metrics_list.append(fake_metrics)
                metrics_file = f'fake_metrics.{format}'

                
                self.d.streaming_data(fake_metrics)

                
            time.sleep(30) 

    def init_fake_data(self, format):
        self.generate_fake_users()
        users_file = f'fake_users.{format}'
        with open(users_file, "w") as file:
            json.dump(self.users_list, file)
        print(f"Fake users have been exported to {users_file}")

        self.generate_fake_sites()
        sites_file = f'fake_sites.{format}'
        with open(sites_file, "w") as file:
            json.dump(self.sites_list, file)
        print(f"Fake sites have been exported to {sites_file}")

        threading.Thread(target=self.generate_fake_metrics(format)).start()
        metrics_file = f'fake_metrics.{format}'
        with open(metrics_file, "w") as file:
            json.dump(self.metrics_list, file)
        print(f"Fake metrics have been exported to {metrics_file}")

 

            
        
            
fake_data_generator = GenerateFakeData()
fake_data_generator.init_fake_data('json')

