from django.contrib import admin
from hospitalapp.models import *
# Register your models here.
class Doctors_DataAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_Department')
    list_filter = ('doc_present_working_status','doc_Department')


class Patient_DataAdmin(admin.ModelAdmin):
    list_display = ('Patient_name', 'Patient_Department')
    list_filter = ('Patient_Id_No','patient_create_date')

class Patient_signAdmin(admin.ModelAdmin):
    list_display = ('Patient_username', 'Patient_Password')


admin.site.register(Doctors_Data,Doctors_DataAdmin)

admin.site.register(Patient_Data,Patient_DataAdmin)

admin.site.register(Patient_Signup,Patient_signAdmin)
