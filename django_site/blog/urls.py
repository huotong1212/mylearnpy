from django.conf.urls import url,include
from django.contrib import admin

from blog import views

urlpatterns = [

    url(r'test/(\d{4})$',views.mytest,name="test"),
    url(r'article/(\d{4})$',views.article_year),

    url(r'article/(?P<year>\d{4})/(?P<month>\d{2})',views.article_year_month),
    url(r'article/(?P<year>\d{4})/(?P<month>\d{2})/\d+',views.article_year_month),

    url(r"baseindex/", views.baseindex),
    url(r"register",views.register,name="reg"),
    url("index/",views.index,name="ind"),
    url(r"login/", views.login, name="log"),
    url(r"student/", views.student),

    url("orm_index2/", views.orm_index),
    url(r"orm_addbook/", views.add_book),
    url(r"orm_updatebook/", views.update_book),
    url(r"orm_delbook/", views.del_book),
    url(r"orm_selectbook/", views.sel_book),
]