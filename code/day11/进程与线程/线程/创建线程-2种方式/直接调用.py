import threading
import time


def sayhi(num):  # 定义每个线程要运行的函数

    print("running on number:%s" % num)

    time.sleep(3)
    print('end sayhi')

def sayhello(num):  # 定义每个线程要运行的函数

    print("running on number:%s" % num)

    time.sleep(3)
    print('end sayhello')


if __name__ == '__main__':
    t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
    t2 = threading.Thread(target=sayhello, args=(3,))  # 生成另一个线程实例

    t1.start()  # 启动线程
    t2.start()  # 启动另一个线程

    t1.join()
    print('t1.join 结束了')
    t2.join()
    print('t2.join 结束了......')
    # join的目的还是协调线程之前的运行，让主线程等待t1,t2执行完毕之后，再运行下面的代码

    print(t1.getName())  # 获取线程名
    print(t2.getName())
    print('主。。。。')

