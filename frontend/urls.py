from django.urls import path, re_path
from django.conf.urls import include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.home, name="home"),
    path('profile/', views.user_profile, name="user_profile"),
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
    url(r'^edit_bill/(?P<id>.*)/$', views.edit_bill, name="edit_bill"),
    url(r'^delete_bill/(?P<id>.*)/$', views.delete_bill, name="delete_bill"),
    path('reports_and_feedbacks/', views.report_feedback, name="report_feedback"),
    url(r'^delete_feedback/(?P<id>.*)/$', views.delete_feedback, name="delete_feedback"),
    url(r'^delete_report/(?P<id>.*)/$', views.delete_report, name="delete_report"),
    path('give_prescription/', views.give_prescription,name="give_prescription"),
    path('patient_health/', views.patient_health, name="patient_health"),
    path('assign_nurse/',views.assign_nurse, name="assign_nurse"),
    path('give_report/',views.give_report, name="give_report"),
    path('control_info/',views.control_info, name="control_info"),
    url(r'^delete_assigned_doctor/(?P<id>.*)/$',views.delete_assigned_doctor, name="delete_assigned_doctor"),
    url(r'^delete_assigned_assistant/(?P<id>.*)/$',views.delete_assigned_assistant, name="delete_assigned_assistant"),
    path('company/', views.medicine_company_add, name="medicine_company_add"),
    url(r'^edit_medicine_company/(?P<id>.*)/$', views.edit_medicine_company, name="edit_medicine_company"),
    url(r'^delete_medicine_company/(?P<id>.*)/$', views.delete_medicine_company, name="delete_medicine_company"),
    
]
