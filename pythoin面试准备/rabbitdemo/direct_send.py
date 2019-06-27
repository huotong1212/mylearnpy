import pika
import sys
credentials = pika.PlainCredentials('huotong', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost',credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info' #严重程度,级别

message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()