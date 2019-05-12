
import socket
import optparse
import json
import os,sys

# ip_sort = ('127.0.0.1',8082)
#
# ftp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ftp_client.connect(ip_sort)

STATUS_CODE  = {
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",

    800 : "the file exist,but not enough ,is continue? ",
    801 : "the file exist !",
    802 : " ready to receive datas",

    900 : "md5 valdate success"

}

class ClientHandler():
    def __init__(self):
        self.op = optparse.OptionParser()

        self.op.add_option('-s','--server',dest="server")
        self.op.add_option('-P','--port',dest="port")
        self.op.add_option('-u','--username',dest="username")
        self.op.add_option('-p','--password',dest="password")

        self.options,self.args = self.op.parse_args()
        self.verify_args(self.options,self.args)
        self.make_connection()
        self.mainPath = os.path.dirname(os.path.abspath(__file__))

    def verify_args(self, options, args):
        # 取参数
        server =  options.server
        port = options.port

        # 简单验证
        if int(port) > 0 and int(port) < 65535:
            return True
        else:
            exit('端口号在0-65535之间')


    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server,int(self.options.port)))

    # 与服务端进行交互
    def interactive(self):
        # 登录验证
        # if authenticate():
        if self.authenticate():
            print('begin to interactive.....')
            cmd_info = input("[%s]>>:"%self.current_path).strip()  # put [file] [filetype]

            cmd_list = cmd_info.split()
            if hasattr(self,cmd_list[0]):
                func = getattr(self,cmd_list[0])
                func(*cmd_list)

    def put(self,*cmd_list):
        # put 12.png images
        action,local_path,target_path = cmd_list
        local_path = os.path.join(self.mainPath,local_path)

        file_name = os.path.basename(local_path)
        file_size = os.stat(local_path).st_size

        data = {
            "action":"put",
            "file_name":file_name,
            "file_size":file_size,
            "target_path":target_path
        }

        self.sock.send((json.dumps(data)).encode('utf-8'))

        is_exist = self.sock.recv(1024).decode('utf8')

        has_sent = 0
        if is_exist == "800":
            # 文件已存在，但不完整
            choice = input("the file exists,but is not integrated,continue?[Y/N]")
            if choice.upper() == 'Y':
                self.sock.send("Y".encode('utf8'))
                # 接受position，确定从该位置进行断点续传
                continue_position = self.sock.recv(1024).decode('utf8')
                has_sent += int(continue_position)
            else:
                self.sock.send("N".encode('utf8'))

        elif is_exist == "801":
            # 文件已存在
            print('文件已经存在......')
            return

        f = open(local_path,'rb')
        #
        f.seek(has_sent)
        while has_sent < file_size:
            # 模拟进度条
            self.show_progress(has_sent,file_size)
            # 开始想服务端发送数据
            data = f.read(1024)
            self.sock.send(data)
            has_sent += len(data)
        f.close()
        print("put success")


    # 登录验证
    def authenticate(self):
        if self.options.username is None or self.options.password is None:
            username = input("username:")
            password = input("password:")
            return self.get_auth_result(username,password)
        return self.get_auth_result(self.options.username,self.options.password)

    # 登录验证
    def get_auth_result(self,username,pwd):

        data = {
            "action":"auth",
            "username":username,
            "password":pwd,
        }

        self.sock.send((json.dumps(data)).encode('utf-8'))

        respone = self.response()
        print('response-->',respone["status_code"])

        if respone["status_code"] == 254:
            self.user = username
            self.current_path = self.user
            print(STATUS_CODE[254])
            return True
        else:
            print(STATUS_CODE[respone["status_code"]])


    def response(self):
        data = self.sock.recv(1024).decode('utf-8')
        return json.loads(data)

    def show_progress(self,has,total):
        rate = float(has)/float(total)
        rate_num = int(rate*100)
        sys.stdout.write('%s%% %s\r'%(rate_num,"#"*rate_num))

    def ls(self):
        data = {
            "action":"ls"
        }
        self.sock.sendall(json.dumps(data).encode('utf8'))

        data = self.sock.recv(1024).decode("utf8")
        print("ls--->",data)

    def cd(self,*cmd_list):
        # cd images/ad

        data = {
            "action":"cd",
            "dirname": cmd_list[1]
        }
        self.sock.sendall(json.dumps(data).encode("utf8"))
        data = self.sock.recv(1024).decode("utf8")

        self.current_path = os.path.basename(data)

    def mkdir(self,*cmd_list):
        data = {
            "action":"mkdir",
            "dirname":cmd_list[1]
        }
        self.sock.sendall(json.dumps(data).encode("utf8"))
        data = self.sock.recv(1024).decode("utf8")


ch = ClientHandler()
ch.interactive()







