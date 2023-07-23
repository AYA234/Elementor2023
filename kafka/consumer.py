from confluent_kafka import Consumer 
from dataWriting import DataWriting
import json

class _consumer:
    def __init__(self):
        bootstrap_servers='pkc-e8mp5.eu-west-1.aws.confluent.cloud:9092'
        security_protocol='SASL_SSL'
        sasl_mechanisms='PLAIN'
        sasl_username='YJEH2DWWEGS4NAG4'
        sasl_password='W15jGRctIjexCA7COGqrdwky2q0AHWlWfN70sHiZqxt9Q8m3JDYoXgzjbzaeJQRs'
        self.topic = 'kamatech'  # metics
        self.group_id = 'my_consumer_group'        # Configure the authentication credentials
        self.conf = {

            'bootstrap.servers': bootstrap_servers,
            'security.protocol': security_protocol,
            'sasl.mechanism': sasl_mechanisms,
            'sasl.username': sasl_username,  # Update with your SASL username
            'sasl.password': sasl_password,  # Update with your SASL password
            'group.id': self.group_id,
            
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
                    self.dataWriting.create_usage_per_site(message_dict)
                    print(f"Received message: {type(message_dict)} from topic {message.topic()} on partition {message.partition()}")
        except KeyboardInterrupt:
            self.consumer.close()

d = _consumer()
d.reading_data()
