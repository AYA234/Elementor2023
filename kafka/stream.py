import producer
import datetime

class stream:
    def __init__(self):
        self.producer=producer.producer()
        
    def __format_data(self,data):
        formatted_data = {
            'cpu_percent': data['metrics'].get('cpu_percent'),
            'time': datetime.datetime.fromtimestamp(data['event_time']).strftime('%a, %d %b %Y %H:%M:%S GMT'),
            'site_id' : data['identifier']['site_id'],
            'storage_gb': data['metrics'].get('storage_gb'),
            'ai_tokens_amount':data['metrics'].get('ai_tokens_amount')
            
}
        return formatted_data
            

               

        
    def stream_matric(self,data):
        topic = 'messages'
        formatted_data = self.__format_data(data)
        print(formatted_data.get('site_id'))
        self.producer.writing_data(formatted_data,topic)
        
    def stream_order(self,data):
        topic='messages'


        self.producer.writing_data(data,topic)

