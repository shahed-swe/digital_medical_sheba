from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token
from collections import OrderedDict
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
                'read_only':True,
            },
            'is_doctor':{
                'read_only':True,
            },
            'is_nurse':{
                'read_only':True,
            },
            'is_assistant':{
                'read_only':True,
            },
            'is_admin':{
                'read_only':True,
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
        new_validate_data = {}
        d1 = Dictionary()
        new_validate_data = d1.dictBack(validate_data)
        user = User(
            username = new_validate_data.get("username"),
            first_name = new_validate_data.get("first_name"),
            last_name = new_validate_data.get("last_name"),
            is_patient = True,
            is_active=True
        )
        user.set_password(new_validate_data.get("password"))
        user.save()
        patient = Patient(
            user = user,
            full_name=user.first_name + ' ' + user.last_name,
            address=validate_data['address'],
            age=validate_data['age'],
            phone_no=validate_data['phone_no'],
        )
        patient.save()
        Token.objects.create(user=user)
        return patient

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

class Dictionary:
    def dictBack(self, data):
        for x, y in data.items():
            if type(y) == OrderedDict:
                return dict(y)
            else:
                pass
