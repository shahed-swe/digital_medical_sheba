from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/', views.mylogin, name="mylogin"),
    path('logout/', views.mylogout, name="mylogout"),
    path('crudDoctor/', views.crudDoctor, name="crudDoctor"),
    path('crudNurse/', views.crudNurse, name="crudNurse"),
    path('crudAssistant/', views.crudAssistant, name="crudAssistant"),
]
