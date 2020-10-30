from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['username','is_patient','is_doctor','is_nurse','is_assistant','is_staff','is_superuser']

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Assistant)
admin.site.register(Nurse)