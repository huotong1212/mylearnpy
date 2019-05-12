
# 我们来测试一下（创建完子进程后，主进程所在的这个脚本就退出了，
# 当父进程先于子进程结束时，子进程会被init收养，成为孤儿进程，而非僵尸进程），文件内容

import os
import sys
import time

pid = os.getpid()
ppid = os.getppid()
print ('im father', 'pid', pid, 'ppid', ppid)
pid = os.fork()
#执行pid=os.fork()则会生成一个子进程
#返回值pid有两种值：
#    如果返回的pid值为0，表示在子进程当中
#    如果返回的pid值>0，表示在父进程当中
if pid > 0:
    print ('father died..')
    sys.exit(0)

# 保证主线程退出完毕
time.sleep(1)
print ('im child', os.getpid(), os.getppid())

# 执行文件，输出结果：
# im father pid 32515 ppid 32015
# father died..
# im child 32516 1
#
# 看，子进程已经被pid为1的init进程接收了，
# 所以僵尸进程在这种情况下是不存在的，存在只有孤儿进程而已，孤儿进程声明周期结束自然会被init来销毁。