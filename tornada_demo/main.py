import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("请登录")
        self.render("login.html")

    def post(self, *args, **kwargs):
        v = self.get_argument('username')
        print(v)
        self.redirect('/index.html')

settings = {
    'template_path': 'templates',
    'static_path': 'static',        # Dir中的位置信息
    'static_url_prefix': '/ppp/',   # url中的别名
}

# application对象中封装了：路由信息，配置信息
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login.html", LoginHandler),
        (r"/index.html", MainHandler),
    ],**settings)

if __name__ == "__main__":
    # 创建socket对象
    # sock = socket.socket()
    # inputs = [socket,]
    app = make_app()
    app.listen(8888)

    # 开启 r,w,e = select.select(inputs,)
    tornado.ioloop.IOLoop.current().start()