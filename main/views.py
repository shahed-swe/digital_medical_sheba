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
    
# Create your views here.
def home(request):
    context = {"title":"Home"}
    return render(request,'front/home.html',context)

def about(request):
    context = {"title":"About"}
    return render(request,'front/about.html',context)