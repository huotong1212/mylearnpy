import pika, time

credentials = pika.PlainCredentials('huotong', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost',credentials=credentials))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # time.sleep(20)
    # print(" [x] Done")
    print("method.delivery_tag", method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag) # 重要，告诉生成者我已经接收到消息了，这样RBQ才不会继续把该消息放入队列
    #ackownledgement

# task_queue
channel.basic_consume('hello',
                        callback,
                      #no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()