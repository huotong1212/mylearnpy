
import socketserver
import json
import configparser
import os

from conf import settings

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

class ServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('----启动Handler')

        while True:
            print('进入while循环')
            data = self.request.recv(1024).strip()
            # 将json字符串转换为python对象
            data = json.loads(data.decode('utf-8'))
            '''
                {'action':'auth',
                 'username':'wang',
                 'pwc','123'}
            '''
            if data.get("action"):
                if hasattr(self,data.get("action")):
                    func = getattr(self,data.get("action"))
                    func(**data)
                else:
                    print('No actions')
            else:
                print('Invaild cmd')

    def auth(self,**data):
        username = data['username']
        password = data['password']

        user = self.authenticate(username,password)

        if user:
            self.sendresponse(254)
        else:
            self.sendresponse(253)

        print('auth',data)

    def authenticate(self,username,password):
        cfg = configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)
        print('authenticata--->',cfg.sections())
        # if username in cfg:
        if username in cfg.sections():
            if password == cfg[username]['Password']:
                self.user = username
                self.mainPath = os.path.join(settings.BASE_DIR,"home",self.user)
                return username


    # 发送响应给客户端
    def sendresponse(self,status_code):
        response = {"status_code":status_code,"status_mes":STATUS_CODE[status_code]}

        self.request.sendall(json.dumps(response).encode('utf-8'))

        pass

    def put(self,**data):
        print("data",data)
        file_name = data["file_name"]
        file_size = data["file_size"]
        target_path = data.get("target_path")

        abs_path = os.path.join(self.mainPath,target_path,file_name)

        has_reveice = 0
        # 判断该文件是否存在
        if os.path.exists(abs_path):
            file_has_size = os.stat(abs_path).st_size
            if file_has_size < file_size:
                # 断点续传
                self.request.sendall("800".encode('utf8'))
                choice = self.request.recv(1024).decode('utf8')
                if choice == 'Y':
                    # 用户决定断点续传
                    f = open(abs_path,'ab')
                    # 告诉客户端从哪个位置开始上传
                    self.request.sendall(str(file_has_size).encode('utf8'))
                    # 让服务端从该位置开始拼接
                    has_reveice += file_has_size
                else:
                    # 用户不想续传，要重新上传
                    f = open(abs_path,'wb')

            elif file_has_size == file_size:
                # 文件存在
                self.request.sendall("801".encode('utf8'))
                return
        else:
            # 文件不存在，从头上传
            self.request.sendall('802'.encode('utf8'))
            f = open(abs_path,'wb')


        while has_reveice < file_size:
            try:
                data = self.request.recv(1024)
            except Exception as e:
                print(e)
                print('-----------have broken')
                break
            f.write(data)
            has_reveice += len(data)

        f.close()

    def ls(self,**data):
        file_list = os.listdir(self.mainPath)

        file_str = "\n".join(file_list)
        if not len(file_list):
            file_str = "<empty str>"

        self.request.sendall(file_str.encode("utf8"))

    def cd(self,**data):
        dirname = data.get("dirname")

        if dirname == "..": # 返回上一级
            self.mainPath = os.path.dirname(self.mainPath)
        self.mainPath = os.path.join(self.mainPath,dirname)


        self.request.sendall(self.mainPath.encode('utf8'))

    def mkdir(self,**data):
        dirname = data.get('dirname')
        path = os.path.join(self.mainPath,dirname)
        # 如果文件存在
        if os.path.exists(path):
            self.request.sendall("the file has existed,mkdir failed".encode("utf8"))
        else:
            if "/" in dirname:
                os.makedirs(path)  # 创建多级文件夹
            else:
                os.mkdir(path)  # 创建单级文件夹
























