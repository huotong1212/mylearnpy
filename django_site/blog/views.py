import datetime

from django.shortcuts import render, HttpResponse, redirect
import time
from django.template import RequestContext
from blog.models import *
from django.db.models import Avg,Sum,Count,Max,Min
# Create your views here.


def show_time(request):

    # return HttpResponse("hello")
    t = time.ctime()
    print('request:',request.get_full_path())
    return render(request,"index.html",{"time":t})

def article_year(request,y):

    # print(reversed('test'))
    return HttpResponse(y)

def article_year_month(request,year,month):

    return HttpResponse("year:%s  month:%s"%(year,month))

def register(request):

    if request.method=="POST":
        print(request.POST.get("user"))
        print(request.POST.get("age"))
        if request.POST.get("user") == "yuan":
            return redirect("log")
        return HttpResponse("success!")

    return render(request,"register.html")

def login(requset):
    print(requset.POST)
    name = requset.POST.get("name")
    num = 12
    return render(requset,"login.html",locals())


def mytest(request,year):
    return HttpResponse('mytest'+year)

def index(request):
    name = "hello haiyan"
    i = 200
    l = [11,22,33,44,55]
    d = {"name":"haiyan","age":20}
    # dating = time.ctime()  不可以
    dating = datetime.datetime.now()

    class People(object): #继承元类
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def __str__(self):
            return self.name+str(self.age)
        def dream(self):
            return "你有梦想吗？"
    #实例化
    person_egon = People("egon",10)
    person_dada = People("dada",34)
    person_susan = People("susan",34)
    person_list = [person_dada,person_egon,person_susan]

    return render(request,"index2.html",
                    {
                        "name":name,
                        "i":i,
                        "l":l,
                        "d":d,  #键对应的是模板里的名字。值对应的是上面定义的变量
                        "person_egon":person_egon,
                        "person_dada":person_dada,
                        "person_list":person_list,
                        "dating":dating,
                    }
              )
    # return render(request,"index2.html",locals())
    #用locals()可以不用写上面的render了。不过用locals()，views里面用什么名。模板里面就得用什么名
    # locals()局部的：用了locals就相当于都得按照上面的那样

def baseindex(requset):
    num = 12
    return render(requset,"baseindex.html",locals())

def student(request):
    student_list = ['Jack','Tom','Daniel']

    return  render(request,"student.html",locals())

def orm_index(request):
    return render(request,"ORM/index.html")

def add_book(request):
    # book1 = Book(price="99",author="yuan",title="python基础",publishDdata="2019-05-02")
    # book1.save()
    Book.objects.create(price="95",author="mask",title="c#基础",publishDdata="2019-05-03")

    return HttpResponse("添加成功")

def update_book(request):
    # Book.objects.filter(nid = '2').update(price=9.8)

    book = Book.objects.get(nid = '2')
    book.price = 9.7
    book.save()

    return HttpResponse("修改成功")

def del_book(request):
    Book.objects.filter(nid='3').delete()
    return HttpResponse('删除成功')

def sel_book(request):
    # book_list = Book.objects.filter(author="yuan")
    # book_list = Book.objects.all()
    # book_list = Book.objects.all()[:2]
    # book_list = Book.objects.all()[::2]

    # book = Book.objects.get(price=95)
    # book_titles = Book.objects.filter(author="yuan").values("title","price")
    # book_titles = Book.objects.filter(author="yuan").values_list("title","price")
    # print(book_titles)

    # book_list = Book.objects.exclude(author="yuan")
    # book_list = Book.objects.all().values('title','price','author').distinct()
    # book_count = Book.objects.all().values('title','price','author').count()
    # print(book_count)

    # book_list = Book.objects.filter(price__gt=50)


    book_list = Book.objects.filter(title__contains = "o")
    return render(request,"ORM/index.html",{"book_list":book_list})
