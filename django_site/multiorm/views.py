from django.http import HttpResponse
from django.shortcuts import render
from multiorm.models import *
from django.db.models import Avg,Sum,Count,Max,Min
from django.db.models import F,Q
# Create your views here.

def index(request):
    return render(request, "ORM/index2.html")

def orm_addbook(request):
    # Book.objects.create(name="linux运维", price=77, pub_date="2017-12-12", publish_id=2)

    # publish_obj = Publish.objects.filter(name="南方出版社")[0]
    # Book.objects.create(name="oracle基础", price=78, pub_date="2017-12-12", publish=publish_obj)

    pubObj = Publish.objects.get(name="人大出版社")  # 只有一个的时候用get,拿到的直接就是一个对象
    bookObj = Book(name="真正的勇士", pub_date="2015-9-9", price="50", publish=pubObj)
    bookObj.save()

    return HttpResponse("添加成功")

def orm_selectbook(request):

    # 使用对象查询
    ''' 正向查询
        #先拿到book对象
        book_obj = Book.objects.get(name="python")
        # 找到对应的出版社对象,是publish类的实例对象
        pub_obj = book_obj.publish
        print(pub_obj.name,pub_obj.city)

        pub_obj = Publish.objects.filter(name="人大出版社").first()
        # bookset = Book.objects.filter(publish = pub_obj).values("name","price")
        bookset = pub_obj.book_set.all().values("name","price")
        print(bookset)

        # 使用双下划线和filter values
        # 人大出版社出版过的书籍与价格
        ret = Book.objects.filter(publish__name = '人大出版社').values("name","price")
        # python这本书出版社的名字
        ret = Publish.objects.filter(book__name='python').values("name")
        ret = Book.objects.filter(name='python').values("publish__name")
        # 北京的出版社出版书的名字
        ret = Book.objects.filter(publish__city='北京').values("name","price")
        # 2019年5月上半旬出版过书的出版社的名字
        ret = Book.objects.filter(pub_date__lt="2019-05-17",pub_date__gt="2019-05-01").values('name','publish__name','publish__city')
        ret = Publish.objects.filter(book__pub_date__lt="2019-05-17",book__pub_date__gt="2019-05-01").values('book__name','name','city')
        print('ret',ret)

    # 多对多
    # 先创建一本书：
    # pub_obj = Publish.objects.filter(name="南方出版社").first()
    # book_obj = Book.objects.create(name="醉玲珑", pub_date="2015-4-10", price="222", publish=pub_obj)
    book_obj = Book.objects.get(name='go')
    # #通过作者的名字django默认找到id
    # yu_obj = Author.objects.filter(name="余光中")[0]
    # han_obj = Author.objects.filter(name="韩寒")[0]
    # hai_obj = Author.objects.filter(name="海明威")[0]
    # 查出所有作者
    auther_list = Author.objects.all()
    # 绑定多对多的关系、
    book_obj.authors.add(*auther_list)

    --- remove clear清楚关系

    # 找到书
    book_obj = Book.objects.get(name='go')
    # 找到所有满足条件的作者
    auther_list = Author.objects.filter(id__gt=3)
    # 使用remove清楚关系
    book_obj.authors.remove(*auther_list)
    # 使用clear清楚所有
    # book_obj.authors.clear()

    # 查询莫言写的所有书
    book_list = Book.objects.filter(authors__name="莫言").values()
    # print('book_list',book_list)
    # ret = Author.objects.filter(name="莫言").values("book__name","book__price")

    # 查询年龄小于50的作者出版过的所有书以及出版社的名称
    ret = Book.objects.filter(authors__age__lt=50).values('publish__name','name','publish__book__name')

    # 查询韩寒出过的所有书及出版社的名称
    au_obj = Author.objects.filter(name='韩寒').first()
    ret = au_obj.book_set.all().values("name","publish__name")
    print('ret',ret)

    book_obj = Book.objects.filter(name="python").first()
    author_list = Author.objects.all()
    print(book_obj.authors)
    print(type(book_obj.authors))
    print(book_obj.authors.all())
    book_obj.authors.add(*author_list)

     # 查询韩寒出过的所有书及出版社的名称
    au_obj = Author.objects.get(name='韩寒')
    # ret = au_obj.book_set.all().values("name", "publish__name")
    # print('ret', ret)
    au_obj.book_set
    print(au_obj.book_set)
    print(au_obj.book_set.all())
    book_obj = Book.objects.get(name="python")
    book_obj.authors

    # 查询所有图书的平均价格
    ret = Book.objects.all().aggregate(Avg('price'))
    ret = Book.objects.all().aggregate(avgPrice = Avg('price')) #加别名

    # 查询人大出版社的书的最低价格
    ret = Book.objects.filter(publish__name='人大出版社').aggregate(最低价格=Min('price'))

    # 查询韩寒写了多少本书
    ret = Book.objects.filter(authors__name='韩寒').aggregate(Count('price'))
    '''

    # 每个作者有多少本书
    ret = Book.objects.values('authors__name').annotate(Count('price'))
    # 每个作者书的总价
    ret = Book.objects.values('authors__name').annotate(authorSum = Sum('price'))

    # 每本书有多少个作者
    # 思路是先 select *,count(author.'name') from ... 然后再取各个authorNum
    # print(Book.objects.all().annotate(authorNum = Count("authors__name")).values("authorNum"))

    # booklist = Book.objects.all().annotate(authorNum=Count("authors__name"))
    # for book_obj in booklist:
    #     print(book_obj.name, book_obj.authorNum)

    # 思路:先按照出版社名字分组，再求出各组的最小价格
    ret = Book.objects.values('publish__name').annotate(Min('price'))
    # 思路：直接求出每个出版社的最小价格，再通过values取出来
    # ret = Publish.objects.all().annotate(minPrice = Min('book__price')).values('name','minPrice')

    # 思路：先求关系表中每一行作者所对应的书名，然后再根据每一组里的任意字段Count出该组是数目
    # ret = Author.objects.values('book__name').annotate(Count('book__price'))

    # 统计包含p的书的作者个数
    # 先筛选出包含p的书，再给每行加上Count字段计算该书的作者个数，最后取出字段name和booCount
    ret = Book.objects.filter(name__contains='p')\
        .annotate(booCount = Count('authors__name')).values('name','booCount')

    # 统计作者大于1的书 .values('authors__name')
    # 先给每个书加上bookCount字段计算他们的值，再筛选出该字段大于1的书
    ret = Book.objects.annotate(bookCount=Count('authors__name')).filter(bookCount__gt=1)

    # 根据一本图书作者数量的多少对查询集QuerySet进行排序:
    ret = Book.objects.annotate(bookCount=Count('authors__name')).order_by('bookCount').values('name','bookCount')


    # 查询各个作者出的书的总价格:
    ret = Book.objects.values('authors__name').annotate(Sum('price'))

    ret = Author.objects.values('name').annotate(Sum('book__price'))
    ret = Author.objects.annotate(bsum = Sum('book__price')).values('name','bsum')


    print(ret)
    # book_list = Book.objects.filter(authors__name="莫言").values()
    return render(request, "ORM/index2.html")

def FQ_book(request):
    # 利用F更新所有价格
    # Book.objects.all().update(price=F('price')-10)

    # 查询出cost < price-10 的书籍
    # ret = Book.objects.filter(cost__lt=F('price')-10)

    # 查询ID大于4且价格大于100的书
    # ret = Book.objects.filter(id__gt=4,price__gt=100)
    # ret = Book.objects.filter(id__gt=4).filter(price__gt=100)
    ret = Book.objects.filter(Q(id__gt=4)&Q(price__gt=100))

    # 查询ID小于3或者价格大于100的书
    ret = Book.objects.filter(Q(id__lt=3)|Q(price__gt=100))

    # 查询年份不是2019或者price大于100的书
    ret = Book.objects.filter(~Q(pub_date__year=2019)|Q(price__gt=100))

    print('ret',ret)

    return render(request, "ORM/index2.html")
