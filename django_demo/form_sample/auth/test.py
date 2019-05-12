from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponse


def auth_01(request):
    User = authenticate(username='huotong',password='879662581')
    print("User:",User)
    if User:
        return HttpResponse("验证成功")
    else:
        return HttpResponse("验证失败")