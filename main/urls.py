from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include
router = routers.DefaultRouter()
router.register(r'patient_user',views.PatientViewSet)
router.register(r'normal_user',views.UserViewSet)



urlpatterns = [
    path('',views.home, name="home"),
    path('user/',include(router.urls)),
]
