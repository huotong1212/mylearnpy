from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app01 import models


def get_student(request):
    stu_list = models.Student.objects.all()
    print('--getstudents',stu_list) # student.cs.title 通过对象去取
    return render(request,"get_students.html",{"stu_list":stu_list})

def add_students(request):
    print('----------add_students')
    if request.method == 'GET':
        cs_list = models.Classes.objects.all()
        return render(request,'add_students.html',{"cs_list":cs_list})
    if request.method == 'POST':
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cs = request.POST.get('cs')
        print('cs',cs)
        cs = models.Classes.objects.get(id=cs)
        models.Student.objects.create(username=username,age=age,gender=gender,cs=cs)
        return redirect('/app01/students.html')

def edit_students(request):
    id = request.GET.get('nid')
    print('----------edit_students',id)
    if request.method == 'GET':
        obj = models.Student.objects.get(id = id)
        cls_list = models.Classes.objects.all()

        return render(request,'edit_students.html',{"obj":obj,"cls_list":cls_list})
    if request.method == 'POST':
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        class_id = request.POST.get('class_id')
        cs = models.Classes.objects.get(id=class_id)
        models.Student.objects.filter(id=id).update(username=username,age=age,gender=gender,cs=cs)
        return redirect('/app01/students.html')

def del_student(request):
    nid = request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    print('del_student,nid',nid)
    return redirect('/app01/students.html')

def ajax_del(request):
    nid = request.GET.get('nid')
    msg = "成功"
    try:
        models.Student.objects.filter(id=nid).delete()
    except Exception as e:
        mag = str(e)
    return HttpResponse(msg)

class CustomPaginator(Paginator):
    pass


def get_student2(request):
    stu_list = models.Student.objects.all()
    print('--getstudents',stu_list) # student.cs.title 通过对象去取

    # 全部数据：USER_LIST，=》得出共有多少条数据
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象（是否具有下一页；是否有上一页；）
    current_page = int(request.GET.get('p'))
    # 创建Paginator对象
    paginator = Paginator(stu_list,3)

    # 拿到page对象并处理异常
    try:
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表，已经切片好的数据
        # number                当前页
        # paginator             paginator对象
        posts = paginator.get_page(current_page)
        # posts = paginator.page(current_page) 该方法没有自动处理异常
    except PageNotAnInteger:
        # 如果是非法字符，显示第一页
        posts = paginator.get_page(1)
    except EmptyPage:
        # 如果是空，显示最后一页
        posts = paginator.get_page(paginator.num_pages)

    return render(request,"index.html",{"posts":posts})