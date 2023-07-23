from confluent_kafka import Consumer
from dataWriting import DataWriting
import json

class consumer:
    def __init__(self):
        self.bootstrap_servers = 'localhost:9092'
        self.topic = 'messages' 
        self.group_id = 'my_consumer_group' 
        self.conf = {
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': self.group_id
        }
        self.consumer = Consumer(self.conf)
        self.consumer.subscribe(topics=[self.topic])
        self.dataWriting = DataWriting()
    def writing_order(self,data):
    
        Site_id=(data['Site_id'])
        User_id=(data["User_id"])
        Package=data['Package']
        if Package == "Free" :
            package_id = 1;
    
        if Package == "Essential":
            package_id = 2;

        if Package == "Advanced":
            package_id = 3;
       
        if Package == "Expert":
            package_id = 4;
        
        packages_to_users_data = {
            
            "user_id":User_id ,
            "package_id": package_id  
        }
        existing_user = self.dataWriting.get_user(User_id)
        if not existing_user:
            self.dataWriting.create_user({'user_id':User_id})
        existing_site=self.dataWriting.get_site(Site_id)
        if not existing_site:
            self.dataWriting.create_site({'site_id':Site_id,'user_id':User_id})
        id=self.dataWriting.create_package_to_user(packages_to_users_data)
        
        sites_to_package_data = {
            
            "package_id": id,  
            "site_id": Site_id
        }
        self.dataWriting.create_sites_to_package(sites_to_package_data)
    def read_matric(self):
        try:
            while True:
                message = self.consumer.poll(timeout=1.0)
                if message is None:
                    continue
                if message.error():
                    print(f"Error: {message.error()}")
                    continue
                message_value = message.value()
                print(f"Received message value: {message_value} on partition {message.partition()}")
                if message_value:
                    message_dict = json.loads(message_value.decode('utf-8'))
                    self.dataWriting.create_usage_per_site(message_dict)
                    print(f"Received message: {type(message_dict)} from topic {message.topic()} on partition {message.partition()}")
        except KeyboardInterrupt:
            self.consumer.close()


    def read_orders(self):
        try:
            while True:
                message = self.consumer.poll(timeout=1.0)
                if message is None:
                    continue
                if message.error():
                    print(f"Error: {message.error()}")
                    continue
                message_value = message.value()
                print(f"Received message value: {message_value} on partition {message.partition()}")
                if message_value:
                    message_dict = json.loads(message_value.decode('utf-8'))
                    print(f"Received message: {message_dict} from topic {message.topic()} on partition {message.partition()}")
                    self.writing_order(message_dict)
                    
        except KeyboardInterrupt:
            self.consumer.close()
d = consumer()
d.read_matric()
