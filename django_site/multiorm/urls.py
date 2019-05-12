
from multiorm import views
from django.conf.urls import url,include

urlpatterns = [
    url(r'index/', views.index),
    url(r'orm_addbook/', views.orm_addbook),
    url(r'orm_selectbook/', views.orm_selectbook),
    url(r'FQ_book',views.FQ_book)
]