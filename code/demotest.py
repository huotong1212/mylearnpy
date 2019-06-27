from celery学习.celeryServer.demo01 import add

t1 = add.delay(4,5)
result = t1.get()

print(result)