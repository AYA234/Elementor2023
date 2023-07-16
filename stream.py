import producer

class _stream:
    def __init__(self):

        self.producer=producer._producer()

    def __format_data(self,data):
            formatted_data = {
    'cpu_percent': data['metrics'].get('cpu_percent', 0.0),
    'disc_a_gb': data['metrics'].get('disc_a_gb', 0.0),
    'disc_b_gb': data['metrics'].get('disc_b_gb', 0.0),
    'disc_cache': data['metrics'].get('disc_cache', 0.0),
    'time': 'Tue, 04 Jul 2023 12:57:44 GMT',
    "id": data['metrics'].get('id'),
    'site_id': 1,
    'storage_gb': data['metrics'].get('storage_gb', 0.0),
    'cpu_tic' :data['metrics'].get('cpu_tic', 0.0)
}
            return formatted_data
            
  
               

        
    def streaming_data(self,data):
        formatted_data = self.__format_data(data)
        print(formatted_data.get('site_id'))
        self.producer.writing_data(formatted_data)
        
