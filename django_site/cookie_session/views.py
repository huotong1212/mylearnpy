from django.http import HttpResponse
from django.shortcuts import render,redirect

from cookie_session.models import *
# Create your views here.

def login(request):
    print('session',request.session)
    print('cookie',request.COOKIES)
    print('login-----session---username',request.session.get('username'))

    print("haslogined",request.COOKIES.get('haslogined',None))
    print("islogined",request.COOKIES.get('islogined',None))

    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')

        ret = User.objects.filter(name=name,pwd=pwd)
        print('ret',ret)
        if ret.exists():
            # cookie_set =  redirect("/cs/index/")
            # cookie_set.set_cookie("username",name)
            # cookie_set.set_cookie("pwd",pwd)
            # cookie_set.set_cookie("haslogined",True)

            # 设置session内部的字典内容,该部分内容会存入django_session数据库
            request.session['islogined'] = True
            request.session['username'] = name

            return redirect("/cs/index/")
    return render(request, "CS/login.html")

def index(request):
    print('index------session', request.session)
    print('index------cookie', request.COOKIES)
    print("index-----islogined",request.session.get('islogined',False))
    print('index-----session---username',request.session.get('username'))

    if request.session.get('islogined',False):
        # 获取字典的内容并传入页面文件
        cookie_content = request.COOKIES
        session_content = request.session
        username = request.session['username']

        return render(request, 'CS/index.html', locals())


    return redirect("/cs/login/")

def logout(request):
    try:
        # del request.session['islogined']
        request.session.flush()  # 删除django-session表中的对应一行记录
    except KeyError as e:
        print('KeyError异常')
        pass
    return redirect('/cs/login/')

from django.views import View
class CBV(View):
    def get(self,request):
        return HttpResponse('CBV.get')

    def post(self,request):
        return HttpResponse('CBV.post')