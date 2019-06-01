import json

from django import forms
from django.forms import fields
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


class F1Form(forms.Form):
    user = fields.CharField(
        # max_length=32,
        # min_length=6,
        required=True,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '太长了',
            'min_length': '太短了',
            'invalid':'用户名无效'
        }
    )
    pwd = fields.CharField(required=True)
    email = fields.EmailField(required=True,error_messages={'invalid':'邮箱格式错误',})
    age = fields.IntegerField(required=True)

def f1(request):
    if request.method == 'GET':
        obj = F1Form()
        return render(request,"form/f1.html",{'obj':obj})
    elif request.method == 'POST':
        print('--------', request.body)
        print('--------',request.POST)
        obj = F1Form(request.POST)
        # 检查是否验证成功
        if obj.is_valid():
            # 用户提交的数据
            data = obj.cleaned_data
            print('验证成功', obj.cleaned_data)
            return HttpResponse(str(data))
        else:
            # 失败错误信息
            print('验证失败', obj.errors)
            error = obj.errors
            return render(request,"form/f1.html",{"obj":obj})

def upload_file(request):
    if request.method == 'GET':
        return render(request, 'form/upload.html')
    else:
        file = request.FILES.get('img')
        filename = file.name
        f = open(filename,"wb")
        for line in file.chunks():
            f.write(line)
        f.close()
        return HttpResponse("提交成功")

def index(request):
    return  render(request,"ajax/index.html")

def ajax_get(request):
    print('Ajax,GET',request.GET)
    # return HttpResponse("ajax_get success")
    ret = {'status':True, 'msg': '....','token':'abc'}
    import json
    import time
    time.sleep(3)
    return HttpResponse(json.dumps(ret))
def ajax1(request):
    import time
    print(request.body)
    # print(request.body.user)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    # print(request.body)
    ret = {'status':True, 'message': '....'}
    import json
    return HttpResponse(json.dumps(ret))

def upload(request):
    return render(request,'upload.html')


def upload_img(request):
    import os
    import uuid

    nid = str(uuid.uuid4())
    ret = {'status':True,'data':None,'message':None}
    obj = request.FILES.get('k3')

    file_path = os.path.join('static', nid+obj.name)
    f = open(file_path,'wb')
    for line in obj.chunks():
        f.write(line)
    f.close()
    ret['data'] = file_path
    return HttpResponse(json.dumps(ret))

def jsonp(request):
    return render(request,'jsonp.html')

def ajax3(request):
    return HttpResponse('本服务器发送的请求')
