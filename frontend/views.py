from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from main.models import *
import requests
from . import forms
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    elif request.user.is_patient:
        return redirect('patient/')
    total_user = len(User.objects.all())
    total_patient = len(Patient.objects.all())
    total_medicine = len(Medicine.objects.all())

    # url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    # api_key = "ec47c902d7798b639246714c56a0d4ef"
    # city = 'Tangail'
    # city_weather = requests.get(url.format(city,api_key)).json()
    # # print(city_weather)
    # weather = {
    #     'city' : city,
    #     'temperature' : int(city_weather['main']['temp']) // 10,
    #     'description' : city_weather['weather'][0]['description'],
    #     'icon' : city_weather['weather'][0]['icon']
    # }
    weather = {
        'temperature' : 300.56 // 10,
    }
    bill = total_bill(Bill.objects.all())
    problem = total_problem()
    released = total_released_patient()
    doctors = len(Doctor.objects.all())
    assistant = len(Assistant.objects.all())
    context = {
        "total_user": total_user,
        "total_patient":total_patient,
        "total_medicine":total_medicine,
        "weather":weather,"title":"Digital Sheba",
        'total_bill':bill,
        "total_problem":problem,
        'total_released':released,
        'total_doctors':doctors,
        'total_assistant':assistant,
        }
    return render(request, 'front/home_page.html' ,context)

def mylogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        utxt = request.POST.get('username')
        upass = request.POST.get('password')
        # print(utxt, upass)
        if utxt != '' and upass != '':
            user = authenticate(username=utxt, password=upass)
            if user !=  None:
                login(request, user)
                return redirect('/')
        else:
            return redirect('/login')
    context = {"title":"Login"}
    return render(request, 'front/login.html', context)

def mylogout(request):
    logout(request)
    return redirect('/login')

def total_bill(take):
    bill_summation = 0
    for i in take:
        bill_summation += int(i.bill)
    return bill_summation

def total_problem():
    total_feedback = len(Feedback.objects.all())
    total_pr = len(ReportProblem.objects.all())
    total = total_feedback + total_pr
    return total

def total_released_patient():
    patient = len(Patient.objects.filter(released=True))
    return patient

def crudDoctor(request):
    if request.user.is_authenticated and request.user.is_superuser:
        doctor = Doctor.objects.all()
        context = {"title":"Manage Doctors","doc":doctor}
        return render(request, 'front/crud_doctor.html', context)
    else:
        return redirect('/')
    
def crudNurse(request):
    if request.user.is_authenticated and request.user.is_superuser:
        nurse = Nurse.objects.all()
        context = {"title":"Manage Doctors","doc":nurse}
        return render(request, 'front/crud_nurse.html', context)
    else:
        return redirect('/')

def crudAssistant(request):
    if request.user.is_authenticated and request.user.is_superuser:
        assistant = Assistant.objects.all()
        context = {"title":"Manage Doctors","doc":assistant}
        return render(request, 'front/crud_doctor.html', context)
    else:
        return redirect('/')