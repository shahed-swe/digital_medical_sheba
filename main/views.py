from django.shortcuts import render
from . import serializers
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework import viewsets,status

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.patientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.doctorSerializer

class NurseViewSet(viewsets.ModelViewSet):
    queryset = models.Nurse.objects.all()
    serializer_class = serializers.nurseSerializer

class AssistantViewSet(viewsets.ModelViewSet):
    queryset = models.Assistant.objects.all()
    serializer_class = serializers.assistantSerializer

class medicineViewSet(viewsets.ModelViewSet):
    queryset = models.Medicine.objects.all()
    serializer_class = serializers.medicineSerializer
    authentication_class = (TokenAuthentication,)
    permission_class = (IsAuthenticated,)

class medicineCompanyViewSet(viewsets.ModelViewSet):
    queryset = models.MedicineCompany.objects.all()
    serializer_class = serializers.medicineCompanySerializer
    authentication_class = (TokenAuthentication,)
    permission_class = (IsAuthenticated,)

class AssignMedicineViewSet(viewsets.ModelViewSet):
    queryset = models.assignMedicine.objects.all()
    serializer_class = serializers.assignMedicineSerializer
    authentication_class = (TokenAuthentication,)
    permission_class = (IsAuthenticated,)
    
class AssignNurseViewSet(viewsets.ModelViewSet):
    queryset = models.assignNurse.objects.all()
    serializer_class = serializers.assignNurseSerializer
    authentication_class = (TokenAuthentication,)
    permission_class = (IsAuthenticated,)
    
class AssignAssistantViewSet(viewsets.ModelViewSet):
    queryset = models.assignAssistant.objects.all()
    serializer_class = serializers.assignAssistantSerializer
    authentication_class = (TokenAuthentication,)
    permission_class = (IsAuthenticated,)

class AssignDoctorViewSet(viewsets.ModelViewSet):
    queryset = models.assignedDoctor.objects.all()
    serializer_class = serializers.assignDoctorSerializer
    authentication_class = (TokenAuthentication,)
    permission_class = (IsAuthenticated,)

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedBackSerializer
    authentication_class = (TokenAuthentication,)
    permission_class = (IsAuthenticated,)


class BillViewSet(viewsets.ModelViewSet):
    queryset = models.Bill.objects.all()
    serializer_class = serializers.BillSerializer
    authentication_class = (TokenAuthentication,)
    permission_class = (IsAuthenticated,)

class ReportViewSet(viewsets.ModelViewSet):
    queryset =  models.ReportProblem.objects.all()
    serializer_class = serializers.ReportSerializer
    authentication_class = (TokenAuthentication,)
    permission_class = (IsAuthenticated,)


