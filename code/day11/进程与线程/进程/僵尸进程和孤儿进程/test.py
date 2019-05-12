from multiprocessing import Process
import time, os


def task():
    print('%s is running' % os.getpid())
    time.sleep(3)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()  # 等待进程p结束后，join函数内部会发送系统调用wait，去告诉操作系统回收掉进程p的id号

    print(p.pid)  # ？？？此时能否看到子进程p的id号
    print('主')

#答案：可以
#分析：
# p.join()是像操作系统发送请求，告知操作系统p的id号不需要再占用了，回收就可以，
# 此时在父进程内还可以看到p.pid,但此时的p.pid是一个无意义的id号，因为操作系统已经将该编号回收
#
# 打个比方：
# 我党相当于操作系统，控制着整个中国的硬件，每个人相当于一个进程，每个人都需要跟我党申请一个身份证号
# 该号码就相当于进程的pid，人死后应该到我党那里注销身份证号，p.join()就相当于要求我党回收身份证号，
# 但p的家人（相当于主进程）
# 仍然持有p的身份证，但此刻的身份证已经没有意义