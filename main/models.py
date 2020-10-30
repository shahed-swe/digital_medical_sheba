from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=True)
    is_nurse = models.BooleanField(default=True)
    is_assistant = models.BooleanField(default=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    phone_no = models.CharField(max_length=50, blank=True, null=True)

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(max_length=120,blank=True,null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50, blank=True,null=True)

class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    full_name = models.CharField(max_length=120,blank=True,null=True)
    degree = models.CharField(max_length=120,blank=True,null=True)
    address = models.CharField(max_length=120,blank=True,null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50,blank=True,null=True)


class Assistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=120, blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50,blank=True,null=True)
