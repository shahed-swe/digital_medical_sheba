from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path('',views.home, name="home"),
]
