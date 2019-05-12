from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01 import models


def get_classes(request):
    cls_list = models.Classes.objects.all()
    print(cls_list)
    return  render(request,'get_classes.html',{"cls_list":cls_list})

def add_classes(request):
    print('----------add_classes')
    if request.method == 'GET':
        return render(request,'add_classes.html')
    if request.method == 'POST':
        title = request.POST.get('title')
        models.Classes.objects.create(title=title)
        return redirect('/app01/classes.html')

def del_classes(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    print('del_classes,nid',nid)
    return redirect('/app01/classes.html')

def edit_classes(request):
    nid = request.GET.get('nid')
    print('---edit',nid)
    if request.method == 'GET':
        obj = models.Classes.objects.get(id=nid)
        return render(request, 'edit_classes.html',{"obj":obj})
    if request.method == 'POST':
        # nid = request.POST.get('nid')
        title = request.POST.get('title')
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('/app01/classes.html')
