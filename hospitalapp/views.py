from django.shortcuts import render
from django.contrib.auth.models import User
from hospitalapp.models import *
from django.contrib.auth import authenticate

# Create your views here.
def patient_login_signup_view(request):
    return render(request,"patient_form.html")


def patient_login(request):
    if request.method == 'POST':
        p_user_name = request.POST.get('uname')
        p_password = request.POST.get('psw')
        mess = Patient_Signup.objects.all()
        mess2 = mess.get(Patient_username=p_user_name)
        mess3 = mess2.Patient_data.Patient_address

        if mess.filter(Patient_username=p_user_name) and mess.filter(Patient_Password=p_password):
            print("sucess")
            return render(request,"patientviewdata.html", {"message":mess, "mess2":mess3})
        else:
            return render(request,"patient_form.html",{"message":"message"})

