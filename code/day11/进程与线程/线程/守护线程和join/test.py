from threading import Thread
import threading
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("虽然主线程和foo都打印了，但主线程还活着，守护线程foo执行完毕已经死掉了,count", threading.active_count())
    print("end456")


t1=Thread(target=foo)
t2=Thread(target=bar)

t1.daemon=True
t1.start()
t2.start()
print("count", threading.active_count())
print("main-------")
