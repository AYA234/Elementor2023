from confluent_kafka import Producer
import json
class _producer():
    def __init__(self):       
        self.bootstrap_servers='localhost:9092'
        self.topic= 'messages'  
        self.conf_producer = {'bootstrap.servers': self.bootstrap_servers}
        self.producer= Producer(self.conf_producer)
        
        

    def writing_data(self, data):
        def delivery_report(err, msg):        
            if err is not None:
                print(f'Message delivery failed: {err}')
            else:
                print(f'Message delivered to {msg.topic()} [{msg.partition()}],{msg}')
        message = json.dumps(data)
        
        self.producer.produce(self.topic, value=message.encode('utf-8'), callback=delivery_report)
        self.producer.flush()
