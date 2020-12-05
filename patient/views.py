from django.shortcuts import render

# Create your views here.
def patient(request):
    return render(request, 'patient.html', {"title":"Patient | Home"})

def login(request):
    return render(request, 'login.html',{"title":"Login"})

def registration(request):
    return render(request, 'registration.html',{"title":'Registration'})