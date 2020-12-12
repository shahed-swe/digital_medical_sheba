from django.urls import path, re_path
from django.conf.urls import include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.home, name="home"),
    path('login/', views.mylogin, name="mylogin"),
    path('logout/', views.mylogout, name="mylogout"),
    path('crudDoctor/', views.crudDoctor, name="crudDoctor"),
    url(r'^edit_doctor/(?P<id>.*)/$', views.edit_doctor , name="edit_doctor"),
    url(r'^delete_doctor/(?P<id>.*)/$', views.delete_doctor , name="delete_doctor"),
    path('crudNurse/', views.crudNurse, name="crudNurse"),
    path('crudAssistant/', views.crudAssistant, name="crudAssistant"),
]
