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
    user = UserSerializer(many=False)
    class Meta:
        model = Doctor
        fields = ['user','full_name','address','age','degree','phone_no']
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
            username = new_validate_data.get('username'),
            first_name = new_validate_data.get("first_name"),
            last_name = new_validate_data.get("last_name"),
            is_doctor = True,
            is_active = True
        )
        user.set_password(new_validate_data.get("password"))
        user.save()
        doctor = Doctor(
            user = user,
            full_name = user.first_name + ' ' + user.last_name,
            address = validate_data['address'],
            age = validate_data['age'],
            degree = validate_data['degree'],
            phone_no = validate_data['phone_no']
        )
        doctor.save()
        Token.objects.create(user=user)
        return doctor

class nurseSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Nurse
        fields = ['user','full_name','degree','age','address','phone_no']
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
            is_nurse = True,
            is_active=True
        )
        user.set_password(new_validate_data.get("password"))
        user.save()
        nurse = Nurse(
            user = user,
            full_name = user.first_name + ' ' + user.last_name,
            address = validate_data['address'],
            age = validate_data['age'],
            degree = validate_data['degree'],
            phone_no = validate_data['phone_no']
        )
        nurse.save()
        Token.objects.create(user=user)
        return nurse


class assistantSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Assistant
        fields = ['user','full_name','address','age','phone_no']
        extra_kwargs = {
            'full_name':{
                'read_only':True
            }
        }
    
    def create(self, validate_data):
        new_validate_data = {}
        d1 = Dictionary()
        new_validate_data = d1.dictBack(validate_data)
        user = User(
            username=new_validate_data.get("username"),
            first_name=new_validate_data.get("first_name"),
            last_name=new_validate_data.get("last_name"),
            is_assistant=True,
            is_active=True
        )
        user.set_password(new_validate_data.get("password"))
        user.save()
        assistant = Assistant(
            user=user,
            full_name=user.first_name + ' ' + user.last_name,
            address=validate_data['address'],
            age=validate_data['age'],
            phone_no=validate_data['phone_no']
        )
        assistant.save()
        Token.objects.create(user=user)
        return assistant


class medicineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineCompany
        fields = '__all__'

class medicineSerializer(serializers.ModelSerializer):
    company_name = medicineCompanySerializer(many=True, read_only=True)
    class Meta:
        model = Medicine
        fields = '__all__'

class assignMedicineSerializer(serializers.ModelSerializer):
    patient = patientSerializer(many=False, read_only=True)
    medicine = medicineSerializer(many=True)
    class Meta:
        model = assignMedicine
        fields = '__all__'

class assignNurseSerializer(serializers.ModelSerializer):
    patient = patientSerializer(many=False, read_only=True)
    nurse = nurseSerializer(many=True)

    class Meta:
        model = assignNurse
        fields = '__all__'

class assignAssistantSerializer(serializers.ModelSerializer):
    doctor = doctorSerializer(many=False)
    # assistant = assistantSerializer(many=False)
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
