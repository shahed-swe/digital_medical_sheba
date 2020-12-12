from django.urls import path, re_path
from django.conf.urls import include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.home, name="home"),
    path('login/', views.mylogin, name="mylogin"),
    path('logout/', views.mylogout, name="mylogout"),
    path('patient/', views.patient, name="patient"),
    url(r'^edit_patient/(?P<id>.*)/$', views.edit_patient, name="edit_patient"),
    url(r'^delete_patient/(?P<id>.*)/$', views.delete_patient, name="delete_patient"),
    path('crudDoctor/', views.crudDoctor, name="crudDoctor"),
    url(r'^edit_doctor/(?P<id>.*)/$', views.edit_doctor , name="edit_doctor"),
    url(r'^delete_doctor/(?P<id>.*)/$', views.delete_doctor , name="delete_doctor"),
    path('crudNurse/', views.crudNurse, name="crudNurse"),
    url(r'^edit_nurse/(?P<id>.*)/$', views.edit_nurse, name="edit_nurse"),
    url(r'^delete_nurse/(?P<id>.*)/$', views.delete_nurse, name="delete_nurse"),
    path('crudAssistant/', views.crudAssistant, name="crudAssistant"),
    url(r'^edit_assistant/(?P<id>.*)/$', views.edit_assistant, name="edit_assistant"),
    url(r'^delete_assistant/(?P<id>.*)/$', views.delete_assistant, name="delete_assistant"),
    path('setbill/', views.set_bill, name="set_bill"),
]
