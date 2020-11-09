from rest_framework import serializers
from .models import *

class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class nurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'

class assistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'


class assignMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignMedicine
        fields = '__all__'

class assignAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignAssistant
        fields = '__all__'

class assignDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = assignedDoctor
        fields = '__all__'

class 