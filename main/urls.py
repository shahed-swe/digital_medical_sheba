from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include
router = routers.DefaultRouter()
router.register(r'úser',views.UserViewSet)



urlpatterns = [
    path('',views.home, name="home"),
    path('user/',include(router.urls)),
]
