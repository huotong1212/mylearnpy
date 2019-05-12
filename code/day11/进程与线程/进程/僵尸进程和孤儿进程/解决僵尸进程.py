# 等待父进程正常结束后会调用wait／waitpid去回收僵尸进程
# 但如果父进程是一个死循环，永远不会结束，那么该僵尸进程就会一直存在，僵尸进程过多，就是有害的
# 解决方法一：杀死父进程
# 解决方法二：对开启的子进程应该记得使用join，join会回收僵尸进程
# 参考python2源码注释

import os

class Process(object):
    def join(self, timeout=None):
        '''
        Wait until child process terminates
        '''
        assert self._parent_pid == os.getpid(), 'can only join a child process'
        assert self._popen is not None, 'can only join a started process'
        res = self._popen.wait(timeout)
        if res is not None:
            _current_process._children.discard(self)