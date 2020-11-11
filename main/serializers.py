from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','is_patient','is_doctor','is_nurse','is_assistant','is_admin']
        extra_kwargs ={
            'password' : {
                'write_only':True,
                'required':True
            },
            'is_patient':{
                'write_only':True,
            },
            'is_doctor':{
                'write_only':True,
            },
            'is_nurse':{
                'write_only':True,
            },
            'is_assistant':{
                'write_only':True,
            },
            'is_admin':{
                'write_only':True,
            }
        }
    def create(self, validate_data):
        user = User.objects.create(**validate_data)
        Token.objects.create(user=user)
        return user

class patientSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Patient
        fields = ['user','full_name','address','age','phone_no']
        extra_kwargs = {
            'full_name':{
                'read_only':True,
            }
        }
    def create(self, validate_data):
        serializer_data = UserSerializer(
            validate_data.user
        ).data
        patient = Patient(
            full_name = user.first_name + ' ' + user.last_name,
            address = validate_data['address'],
            age = validate_data['age'],
            phone_no = validate_data['phone_no']
        )
        patient.save()
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
