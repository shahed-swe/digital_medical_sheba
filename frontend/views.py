from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from main.models import *
from rest_framework.authtoken.models import Token
import requests
from . import forms
from django.http import JsonResponse
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
        if request.method == "POST":
            user = User(
                username = request.POST.get('doctorUsername'),
                first_name = request.POST.get('doctorFirstname'),
                last_name = request.POST.get('doctorLastname'),
                email = request.POST.get('doctorEmail'),
                is_doctor = True,
                is_active = True
            )
            user.set_password(request.POST.get('doctorPassword1'))
            user.save()
            doctor = Doctor(
                user = user,
                full_name = user.first_name+' '+user.last_name,
                address = request.POST.get('doctorAddress'),
                age = request.POST.get('doctorAge'),
                degree = request.POST.get('doctorDegree'),
                phone_no = request.POST.get('doctorPhoneno')
            )
            doctor.save()
            Token.objects.create(user=user)

        return render(request, 'front/crud_doctor.html', context)
    else:
        return redirect('/')

def edit_doctor(request, id):
    doc = Doctor.objects.filter(pk=id)
    user = User.objects.get(pk=id)
    print(user)
    print(doc)
    if request.method == "POST":
        doctor = Doctor(
            user=user,
            full_name=user.first_name+' '+user.last_name,
            address=request.POST.get('doctorAddress'),
            age=request.POST.get('doctorAge'),
            degree=request.POST.get('doctorDegree'),
            phone_no=request.POST.get('doctorPhoneno')
        )
        doctor.save()
        return redirect('/crudDoctor')
    return render(request, 'front/edit_doctor_view.html',{"title":"Edit","doc":doc})

def delete_doctor(request, id):
    doc = Doctor.objects.filter(pk=id)
    user = User.objects.filter(pk=id)
    if request.method == "POST":
        val = request.POST.get('button-value')
        if val == "Yes":
            doc.delete()
            user.delete()
            return redirect('/crudDoctor')
    return render(request, 'front/doctor_delete_view.html',{"title":"Delete"})

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