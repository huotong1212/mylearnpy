from django.conf.urls import url,include

from cookie_session import views

urlpatterns = [
    url(r'login$',views.login,name="log"),
    url(r'index$',views.index),
    url(r'logout$', views.logout),
    url(r'cbv$', views.CBV.as_view()),
]