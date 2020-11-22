from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_assistant = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name+ ' | '+str(self.pk)

class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='user')
    full_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "patient_info"
    
    def __str__(self):
        return self.user.first_name + ' | ' + str(self.user.last_name) +' | '+ str(self.pk)

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='doctoruser')
    user_name = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(max_length=120,blank=True,null=True)
    phone_no = models.CharField(max_length=50, blank=True,null=True)

    class Meta:
        db_table = "doctor_info"
    
    def __str__(self):
        return self.user.first_name + ' | '+str(self.pk)

class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name="nurseuser")
    full_name = models.CharField(max_length=120,blank=True,null=True)
    degree = models.CharField(max_length=120,blank=True,null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=120,blank=True,null=True)
    phone_no = models.CharField(max_length=50,blank=True,null=True)

    class Meta:
        db_table = "nurse_info"

    def __str__(self):
        return self.user.first_name + ' | '+str(self.pk)

class Assistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name="assistantuser")
    full_name = models.CharField(max_length=120, blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=50,blank=True,null=True)

    class Meta:
        db_table = "assistant_info"

    def __str__(self):
        return self.user.first_name + ' | '+str(self.pk)

class MedicineCompany(models.Model):
    company_name = models.CharField(max_length=120,blank=True,null=True)

    class Meta:
        db_table = "medicine_company"

    def __str__(self):
        return self.company_name + " | "+str(self.pk)

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=120,blank=True, null=True)
    company_name = models.ManyToManyField(MedicineCompany, related_name="company")

    class Meta:
        db_table = "medicine_info"

    def __str__(self):
        return self.medicine_name + ' | '+ str(self.id)

class Feedback(models.Model):
    user = models.CharField(max_length=120, blank=True, null=True, default="_")
    feedback = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = "feedback_section"
    
    def __str__(self):
        return self.feedback + ' | '+ str(self.id)

class Bill(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)
    bill = models.CharField(max_length=120,blank=True,null=True)

    class Meta:
        db_table = "billing_information"
    

class assignNurse(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)
    nurse = models.ManyToManyField(Nurse, related_name='assign_nurse')

    class Meta:
        db_table = "assigned_nurse"
    
    def __str__(self):
        return "Nurse Assigned For "+self.patient.full_name+" | "+str(self.pk)

class assignMedicine(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True,related_name="patient_medicine")
    medicine = models.ManyToManyField(Medicine, related_name="assign_medicine")

    class Meta:
        db_table = "assigned_medicine"
    
    def __str__(self):
        return "Medicine Assigned For "+self.patient.user.first_name +" "+self.patient.user.last_name+" | "+str(self.pk)

class assignAssistant(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, primary_key=True)
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE, related_name="assign_assistant")

    class Meta:
        db_table = "assigned_assistant"

    def __str__(self):
        return self.doctor.full_name + ' | '+self.assistant.user.first_name + ' | '+str(self.pk)

class assignedDoctor(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,blank=True, null=True, related_name="assign_doctor")

    class Meta:
        db_table = "assigned_doctor"
    
    def __str__(self):
        return self.patient.user.first_name + ' | '+self.doctor.user.first_name + ' | '+str(self.pk)
