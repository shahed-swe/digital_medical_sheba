from rest_framework import serializers
from .models import *

class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'

class Assistant(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'

