from django.shortcuts import render, redirect
from app01 import models
from app01.a1forms import TeacherForm,ClassForm

def set_teacher(request):
    nid = request.GET.get('nid')
    print('set__teacher',nid)
    if request.method == "GET":
        cls_obj = models.Classes.objects.filter(id=nid).first()
        cls_teacher_list = cls_obj.m.all().values_list('id', 'name')
        # [Teacher obj,obj,obj,]
        # [(1,'hf'),(2,"Al"),(3,'uh')]
        # ==> [1,2,3]
        # 当前班级任课教师的id列表
        id_list = list(zip(*cls_teacher_list))[0] if list(zip(*cls_teacher_list)) else []
        all_teacher_list = models.Teachers.objects.all()
        return render(request,"set_teacher.html",{
            "all_teacher_list":all_teacher_list,
            "nid":nid,
            'id_list': id_list,
        })
    elif request.method == "POST":
        teacher_ids = request.POST.get("teacher_ids")
        print('teacher-post', teacher_ids)
        teacher_list = models.Teachers.objects.filter(id__in = teacher_ids)
        print('teacher_list',teacher_list)
        cls_obj = models.Classes.objects.get(id=nid)
        cls_obj.m.add(*teacher_list)
        return redirect('/app01/classes.html')

def get_teacher_list(request):
    tea_list = models.Teachers.objects.all()
    return render(request,'get_teacher.html',{"tea_list":tea_list})

def edit_teacher(request,nid):
    if request.method == 'GET':
        teacher = models.Teachers.objects.filter(id = nid).first()
        obj = TeacherForm({"name":teacher.name})
        return render(request, "edit_teacher.html", {"obj": obj,"nid":nid})
    elif request.method == 'POST':
        # 拿到POST的表单字典，创建Form对象
        obj = TeacherForm(request.POST)
        # 判断是否验证成功
        if obj.is_valid():
            # 更新
            models.Teachers.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/app01/form_get_teacher')
        else:
            # 否则将数据返回前端，这里再次传入obj是为了保证前端用户输入的数据不丢失
            return render(request, "edit_teacher.html", {"obj": obj})



def add_teacher(request):
    if request.method == 'GET':
        obj = TeacherForm()
        return render(request,"add_teacher.html",{"obj":obj})
    elif request.method == 'POST':
        # 拿到POST的表单字典，创建Form对象
        obj = TeacherForm(request.POST)
        # 判断是否验证成功
        if obj.is_valid():
            # 通过字典生产新的教师对象，生成一条新的教师记录
            models.Teachers.objects.create(**obj.cleaned_data)
            return redirect('/app01/form_get_teacher')
        else:
            # 否则将数据返回前端，这里再次传入obj是为了保证前端用户输入的数据不丢失
            return render(request,"add_teacher.html",{"obj":obj})




















