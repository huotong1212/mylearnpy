import pika
import time

credentials = pika.PlainCredentials('huotong', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost',credentials=credentials))

channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):

    print("received msg...start processing....",body)
    # time.sleep(2)
    # print(" [x] msg process done....",body)


channel.basic_consume('hello',callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()