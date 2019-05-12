
import optparse  # 解析命令行命令
import socketserver

from conf import settings
from core import server

class ArgvHandler():

    def __init__(self):
        self.op = optparse.OptionParser()

        # 设置命令
        self.op.add_option('-s','--server',dest= 'server')
        self.op.add_option('--p','--port',dest='port')
        self.op.add_option('--st', '--start', dest='start')

        # options 对应参数已经设置的命令，以字典形式返回（但不是字典）
        # args 对应没有设置的命令，以列表形式返回（但不是列表）
        options,args = self.op.parse_args()

        self.verify_args(options,args)

    def verify_args(self,options,args):
        cmd = args[0]

        if hasattr(self,cmd):
            func = getattr(self,cmd)
            func()

    def start(self):
        print(" the server is working...")
        s = socketserver.ThreadingTCPServer((settings.IP,settings.PORT),server.ServerHandler)
        s.serve_forever()


    def help(self):
        pass