# 至少要有两个类
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from django_demo import settings


class Md1(MiddlewareMixin):  #必须继承
    def process_request(self,request):
        print("md1===process_request")
        l = ["/login/"]
        l2 = ["/fs/index.html",]
        #request.path_info：当前的路径
        print('request_path_info',request.path_info,type(request.path_info))
        if request.path_info in l2:  #因为login不做验证，就直接返回none就行了
            return None # return None还是会往下执行
        # return HttpResponse("OK") # 这样return就不会执行到下一个M2了
        print('After None')
        # if not request.session.get(settings.GDP):
        #     return redirect("/login/")
        #
        # 如果无返回值，就继续执行后续中间件和视图函数
        # 如果有返回值，就执行自己的process_response和上面的response
    def process_response(self,request,response):
        print("md1====process_response1")
        return response   #必须有返回值

class Md2(MiddlewareMixin):
    def process_request(self,request):
        print("md2====process_request2")
    def process_response(self,request,response):
        print("md2====process_response2")
        return response