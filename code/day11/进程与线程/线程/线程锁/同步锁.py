import time
import threading

def addNum():
    global num #在每个线程中都获取这个全局变量
    # num-=1
    lock.acquire()
    temp=num
    print('--get num:',num )
    time.sleep(0.1)
    num =temp-1 #对此公共变量进行-1操作
    lock.release()

num = 100  #设定一个共享变量
thread_list = []
lock=threading.Lock()

for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

# print('---------------before join') # my
# time.sleep(2) # my
# for i,t in enumerate(thread_list): #等待所有线程执行完毕
#     t.join()
#     if i > 50: # my
#         break # my
#
# print('final num:', num )