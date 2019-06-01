from django.conf.urls import url
from form_sample import views
from form_sample.auth import test

urlpatterns = [
    url(r'^f1.html$',views.f1),
    url(r'^upload.html$', views.upload_file),
    url(r'^ajax1.html$', views.ajax_get),
    url(r'^ajaxpost$', views.ajax1),
    url(r'^index.html$', views.index),
    url(r'^upload_img.html$', views.index),
    url(r'^auth01$', test.auth_01),
    url(r'^auth02$', test.auth_01),
]



















