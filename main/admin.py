from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['username','is_patient','is_doctor','is_nurse','is_assistant','is_admin','is_staff','is_active','is_superuser']

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Assistant)
admin.site.register(Nurse)
admin.site.register(Medicine)
admin.site.register(Feedback)
admin.site.register(Bill)
admin.site.register(assignNurse)
admin.site.register(assignMedicineNew)
admin.site.register(assignAssistant)
admin.site.register(assignedDoctor)
admin.site.unregister(Group)
admin.site.register(MedicineCompany)
admin.site.register(ReportProblem)
admin.site.register(PatientHealthAdd)
admin.site.register(PatientHealthReport)
