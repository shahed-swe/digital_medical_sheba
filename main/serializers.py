from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token


class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        extra_kwargs = {
            'password':{
                'write_only':True,
                'required':True
            }
        }
    
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user

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
