from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.patient, name="patient"),
    path('myregistration/', views.registration, name="registration"),
    path('profile/', views.profile, name="profile"),
    path('medicine/', views.medicine, name="medicine"),
    path('feedback/', views.feedback, name="feedback"),
    path('report/', views.report, name="report"),
]
