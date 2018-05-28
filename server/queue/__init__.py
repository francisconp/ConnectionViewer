import pika

class queue:
    """hostname,queue,routing_key"""
    def __init__(self, **kwargs):
        """hostname,queue"""
        self.hostname = kwargs['hostname']
        self.queue = kwargs['queue']
        self.routing_key = kwargs['queue']

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.hostname))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)
    
    def send(self,data):
        self.channel.basic_publish(exchange='',
                      routing_key=self.routing_key,
                      body=data)
