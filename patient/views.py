from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from main.models import *
from django.http import HttpResponse
# Create your views here.
def patient(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    elif request.user.is_authenticated and request.user.is_superuser:
        return redirect('/')
    elif request.user.is_authenticated and request.user.is_doctor:
        return redirect('/')
    elif request.user.is_authenticated and request.user.is_nurse:
        return redirect('/')
    elif request.user.is_authenticated and request.user.is_assistant:
        return redirect('/')
    else:
        return render(request, 'home.html', {"title":"Patient | Home"})


def registration(request):
    if request.method == "POST":
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(password1, password2)
        if password1 == password2:
            user = User(
                username = request.POST.get('username'),
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                email = request.POST.get('email'),
                is_patient = True,
                is_active = True
            )
            user.set_password(request.POST.get('password1'))
            user.save()
            patient = Patient(
                user = user,
                full_name = user.first_name + ' '+ user.last_name,
                address = request.POST.get('address'),
                age = request.POST.get('age'),
                phone_no=request.POST.get('phone')
            )
            patient.save()
            Token.objects.create(user=user)
        else:
            message = "Password Doesn't match properly"
            context = {"title":"Registration","message":message}
            return render(request, 'registration.html',{'title':'Registration'})
    return render(request, 'registration.html',{"title":'Registration'})