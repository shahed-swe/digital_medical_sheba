from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.patient, name="patient"),
    path('mylogin/', views.login, name="login"),
    path('myregistration/', views.registration, name="registration"),
]
