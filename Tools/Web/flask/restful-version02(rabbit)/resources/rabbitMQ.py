from flask_restful import Resource, reqparse
import pika
from common import config



def connectMQ():
    credentials = pika.PlainCredentials('toby', '1234')
    parameters = pika.ConnectionParameters('toby-rabbit',
                                       5672,
                                       '/',
                                       credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return channel


class Declare (Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('token', required=True, help='token is required')
    parser.add_argument('queue', required=True, help='queue is required')

    def get(self, name):
        pass

    def post(self, name):
        arg = self.parser.parse_args()
        if name == config.users[0]['name'] and arg['token'] == config.users[0]['token']:
            channel = connectMQ()
            channel.queue_declare(queue=arg['queue'])
            return {
                'message': 'Declare ' + arg['queue'] + ' done!',
            }, 200
        else:
            return {
                'message': 'Your token is wrong.',
            }, 200
        
    def put(self, name):
        pass

    def delete(self, name):
        pass


class Producer (Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('token', required=True, help='token is required')
    parser.add_argument('queue', required=True, help='queue is required')
    parser.add_argument('message', required=True, help='message is required')

    def get(self, name):
        pass

    def post(self, name):
        arg = self.parser.parse_args()
        if name == config.users[0]['name'] and arg['token'] == config.users[0]['token']:
            channel = connectMQ()
            channel.basic_publish(exchange='', routing_key=arg['queue'], body=arg['message'])
            return {
                'message': 'Produce message: ' + arg['message'] + ' on queue: ' + arg['queue'] + ' !',
            }, 200
        else:
            return {
                'message': 'Your token is wrong.',
            }, 200
        
    def put(self, name):
        pass

    def delete(self, name):
        pass

class Consumer (Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('token', required=True, help='Token is required')
    parser.add_argument('queue', required=True, help='queue is required')

    def get(self, name):
        pass

    def post(self, name):
        arg = self.parser.parse_args()
        if name == config.users[0]['name'] and arg['token'] == config.users[0]['token']:
            channel = connectMQ()

            def callback(ch, method, properties, body):
                print(" [x] Received %r" % body)
            channel.basic_consume(queue=arg['queue'], on_message_callback=callback, auto_ack=True)
            channel.start_consuming()

            return {
                'message': 'Done!',
            }, 200
        else:
            return {
                'message': 'Your token is wrong.',
            }, 200
        
    def put(self, name):
        pass

    def delete(self, name):
        pass

