from confluent_kafka import Consumer
from dataWriting import DataWriting
import json

class _consumer:
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

    def reading_data(self):
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
                    print(f"Received message: {type(message_dict)} from topic {message.topic()} on partition {message.partition()}")
                    self.dataWriting.create_usage_per_site(message_dict)
        except KeyboardInterrupt:
            self.consumer.close()

d = _consumer()
d.reading_data()
