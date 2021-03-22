from datetime import datetime

from django.db import models

# Create your models here.
class Doctors_Data(models.Model):
    doc_name = models.CharField(max_length=50)
    doc_Department = models.CharField(max_length=50)
    doc_Id_No = models.CharField(max_length=50, primary_key=True)
    doc_experence = models.IntegerField()
    doc_qulification = models.CharField(max_length=100)
    doc_present_working_status = models.BooleanField(default=False)
    doc_address = models.TextField(max_length=200)
    doc_mobile = models.IntegerField()
    doc_email = models.EmailField(default=False)
    doc_create_date = models.DateField(default=datetime.now)


    def __str__(self):
        return "Doctor Name: "+self.doc_name +" "+"Department: "+ self.doc_Department

class Patient_Data (models.Model):
    Patient_name = models.CharField(max_length=50)
    Patient_Department = models.CharField(max_length=50)
    Patient_Id_No = models.CharField(max_length=50, primary_key=True)
    patient_create_date = models.DateField(default=datetime.now)
    Patient_mobile = models.IntegerField()
    Patient_address = models.TextField(max_length=200)
    Patient_email = models.EmailField(default=False)
    def __str__(self):
        return "Patient Name: "+self.Patient_name +" "+"Patient: "+ self.Patient_Id_No

class Patient_Signup (models.Model):
    Patient_username = models.CharField(max_length=20, primary_key=True)
    Patient_Password = models.CharField(max_length=20)
    Patient_data = models.ForeignKey(Patient_Data, on_delete=models.CASCADE)

