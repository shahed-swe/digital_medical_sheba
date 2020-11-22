from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include
router = routers.DefaultRouter()
router.register(r'patient_user',views.PatientViewSet)
router.register(r'doctor_user',views.DoctorViewSet)
router.register(r'nurse_user',views.NurseViewSet)
router.register(r'assistant_user', views.AssistantViewSet)
router.register(r'normal_user',views.UserViewSet)
router.register(r'assign_medicine', views.AssignMedicineViewSet)
router.register(r'assign_nurse', views.AssignNurseViewSet)
router.register(r'assign_assistant', views.AssignAssistantViewSet)
router.register(r'assign_doctor', views.AssignDoctorViewSet)
router.register(r'medicine',views.medicineViewSet)
router.register(r'company',views.medicineCompanyViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
]
