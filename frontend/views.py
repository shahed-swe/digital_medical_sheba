from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from main.models import *
from rest_framework.authtoken.models import Token
import requests
from . import forms
from django.http import HttpResponse
import datetime
# Create your views here.
# for admin panel
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

#for all type of users
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'front/user_profile.html',{"title":"User Profile"})
    else:
        return redirect('/login')
# for all type of users
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

#for all type of users
def mylogout(request):
    logout(request)
    return redirect('/login')

#for some perticuler users, this are not counted as view
def total_bill(take):
    bill_summation = 0
    for i in take:
        bill_summation += int(i.bill)
    return bill_summation

#for some perticuler users, this are not counted as view
def total_problem():
    total_feedback = len(Feedback.objects.all())
    total_pr = len(ReportProblem.objects.all())
    total = total_feedback + total_pr
    return total

#for some perticuler users, this are not counted as view
def total_released_patient():
    patient = len(Patient.objects.filter(released=True))
    return patient

# for admin panel control, to see the list of patient
def patient(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    elif request.user.is_superuser:
        patient = Patient.objects.all()
        return render(request, 'front/patient_control.html', {"title":"Patient","patient":patient})
    else:
        return redirect('/')

# for admin panel control, to edit the patient information
def edit_patient(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    elif request.user.is_superuser:
        pat = Patient.objects.filter(pk=id)
        user = User.objects.get(pk=id)
        if request.method == "POST":
            if request.POST.get('patientRelease') == "on":
                patient = Patient(
                    user=user,
                    full_name=user.first_name+' '+user.last_name,
                    address=request.POST.get('patientAddress'),
                    age=request.POST.get('patientAge'),
                    phone_no=request.POST.get('patientPhoneno'),
                    released = True
                )
                patient.save()
            else:
                patient = Patient(
                    user=user,
                    full_name=user.first_name+' '+user.last_name,
                    address=request.POST.get('patientAddress'),
                    age=request.POST.get('patientAge'),
                    phone_no=request.POST.get('patientPhoneno'),
                    released=False
                )
                patient.save()
            return redirect('/patient')
        return render(request, 'front/edit_patient_view.html',{"title":"Edit","pat":pat})
    else:
        return redirect('/')

# for admin panel control, to delete the patient information
def delete_patient(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    elif request.user.is_superuser:
        patient = Patient.objects.filter(pk=id)
        user = User.objects.filter(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            if val == "Yes":
                patient.delete()
                user.delete()
                return redirect('/patient')
        return render(request, 'front/delete_patient_view.html', {"title": "Delete","patient":patient})
    else:
        return redirect('/')

# crud system for doctor, add and show, for only admin
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

# edit view of doctor, for only admin
def edit_doctor(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        doc = Doctor.objects.filter(pk=id)
        user = User.objects.get(pk=id)
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
    else:
        return redirect('/')

# delete view of doctor, for only admin
def delete_doctor(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        doc = Doctor.objects.filter(pk=id)
        user = User.objects.filter(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            if val == "Yes":
                doc.delete()
                user.delete()
                return redirect('/crudDoctor')
        return render(request, 'front/doctor_delete_view.html',{"title":"Delete","doc":doc})
    else:
        return redirect('/')

# crud system for nurse, only accessible by admin
def crudNurse(request):
    if request.user.is_authenticated and request.user.is_superuser:
        nurse = Nurse.objects.all()
        context = {"title":"Manage Nurse","nurse":nurse}
        if request.method == "POST":
            user = User(
                username = request.POST.get('nurseUsername'),
                first_name = request.POST.get('nurseFirstname'),
                last_name = request.POST.get('nurseLastname'),
                email = request.POST.get('nurseEmail'),
                is_nurse = True,
                is_active = True
            )
            user.set_password(request.POST.get('nursePassword1'))
            user.save()
            nurse = Nurse(
                user = user,
                full_name = user.first_name+' '+user.last_name,
                address = request.POST.get('nurseAddress'),
                age = request.POST.get('nurseAge'),
                degree = request.POST.get('nurseDegree'),
                phone_no = request.POST.get('nursePhoneno')
            )
            nurse.save()
            Token.objects.create(user=user)
        return render(request, 'front/crud_nurse.html', context)
    else:
        return redirect('/')

# edit view of nurse, only accessible for admin
def edit_nurse(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        nur = Nurse.objects.filter(pk=id)
        user = User.objects.get(pk=id)
        if request.method == "POST":
            nurse = Nurse(
                user = user,
                full_name = user.first_name+ ' '+user.last_name,
                address = request.POST.get('nurseAddress'),
                age = request.POST.get('nurseAge'),
                degree = request.POST.get('nurseDegree'),
                phone_no = request.POST.get('nursePhoneno')
            )
            nurse.save()
            return redirect('/crudNurse')
        return render(request, 'front/edit_nurse_view.html',{"title":"Edit Nurse","nur":nur})
    else:
        return redirect('/')

# delete view of nurse, only accessible for admin
def delete_nurse(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        nur = Nurse.objects.filter(pk=id)
        user = User.objects.get(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            if val == "Yes":
                nur.delete()
                user.delete()
                return redirect('/crudNurse')
        return render(request, 'front/delete_nurse_view.html')
    else:
        return redirect('/')

# crud system of assistant, only accessible for admin
def crudAssistant(request):
    if request.user.is_authenticated and request.user.is_superuser:
        assis = Assistant.objects.all()
        context = {"title":"Manage Assistant","assistant":assis}
        if request.method == "POST":
            user = User(
                username = request.POST.get('assistantUsername'),
                first_name = request.POST.get('assistantFirstname'),
                last_name = request.POST.get('assistantLastname'),
                email = request.POST.get('assistantEmail'),
                is_assistant = True,
                is_active = True
            )
            user.set_password(request.POST.get('assistantPassword1'))
            user.save()
            assistant = Assistant(
                user = user,
                full_name = user.first_name+' '+user.last_name,
                address = request.POST.get('assistantAddress'),
                age = request.POST.get('assistantAge'),
                phone_no = request.POST.get('assistantPhoneno')
            )
            assistant.save()
            Token.objects.create(user=user)
        return render(request, 'front/crud_assistant.html', context)
    else:
        return redirect('/')

# edit view of assistant, only accessible for admin
def edit_assistant(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        assis = Assistant.objects.filter(pk=id)
        user = User.objects.get(pk=id)
        if request.method == "POST":
            assistant = Assistant(
                user = user,
                full_name = user.first_name+ ' '+user.last_name,
                address = request.POST.get('assistantAddress'),
                age = request.POST.get('assistantAge'),
                phone_no = request.POST.get('assistantPhoneno')
            )
            assistant.save()
            return redirect('/crudAssistant')
        return render(request,'front/edit_assistant_view.html',{"title":"Update Assistant","assis":assis})
    else:
        return redirect('/')

# delete view of assistant, only accessible for admin
def delete_assistant(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        assis = Assistant.objects.filter(pk=id)
        user = User.objects.get(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            if val == "Yes":
                assis.delete()
                user.delete()
                return redirect('/crudAssistant')
        return render(request, 'front/delete_assistant_view.html', {"title":"Assistant Update","assis":assis})
    else:
        return redirect('/')
# crud operations are successfully done
# for admin panel control set bill, this bill will go to patient
def set_bill(request):
    if request.user.is_authenticated and request.user.is_superuser:
        patient = Patient.objects.all()
        bill = Bill.objects.all()
        if request.method == "POST":
            pat1 = request.POST.get('patient')
            bill2 = request.POST.get('bill')
            if pat1 != "" and bill != "":
                pat2 = Patient.objects.get(pk=pat1)
                bill2 = Bill(
                    patient = pat2,
                    bill = bill2,
                    paid = False
                )
                bill2.save()
        return render(request, 'front/setbill.html',{"title":'Patient Bill',"bill":bill, "pat":patient})
    else:
        return redirect('/')

# edit bill view only accessible for admin
def edit_bill(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        bill = Bill.objects.filter(pk=id)
        if request.method == "POST":
            if request.POST.get('paid') == 'on':
                patient = Patient.objects.get(pk=id)
                bill = Bill(
                    patient=patient,
                    bill=request.POST.get('patientbill'),
                    paid=True
                )
                bill.save()
            else:
                patient = Patient.objects.get(pk=id)
                bill = Bill(
                    patient=patient,
                    bill=request.POST.get('patientbill'),
                    paid=False
                )
                bill.save()
            return redirect('/setbill')
        return render(request, 'front/edit_bill.html', {"title":"Edit Bill", "bill":bill})
    else:
        return redirect('/')

# delete view of bill, only accessible for admin
def delete_bill(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        bill = Bill.objects.filter(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            if val == "Yes":
                bill.delete()
                return redirect('/setbill')
        return render(request, 'front/delete_bill.html', {"bill":bill})
    else:
        return redirect('/')

# reports and feedback, only available for admin and doctor
def report_feedback(request):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_doctor:
        feed = Feedback.objects.all()
        report = ReportProblem.objects.all()
        context = {"feed":feed, "report":report,"title":"Report & Feedback"}
        return render(request, 'front/reports.html',context)
    else:
        return redirect('/')

# report status update only available for admin
def update_report_status(request, id):
    if request.user.is_authenticated:
        rprt = ReportProblem.objects.filter(pk=id).update(solve=True)
        return redirect('/reports_and_feedbacks')
    else:
        return redirect('/')

# feedback status update only available for admin and doctor
def update_feedback_status(request, id):
    if request.user.is_authenticated or request.user.is_doctor:
        fdb = Feedback.objects.filter(pk=id).update(solve=True)
        return redirect('/reports_and_feedbacks')
    else:
        return redirect('/')


# delete view of feedback, only available for admin and doctor
def delete_feedback(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_doctor:
        feed = Feedback.objects.filter(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            if val == "Yes":
                feed.delete()
                return redirect('/reports_and_feedbacks')
        return render(request, 'front/delete_feedback.html', {"feed":feed})
    else:
        return redirect('/')

# delete view of report, only available for admin
def delete_report(request, id):
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_doctor:
        report = ReportProblem.objects.filter(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            if val == "Yes":
                report.delete()
                return redirect('/reports_and_feedbacks')
        return render(request, 'front/delete_report.html', {"report":report})
    else:
        return redirect('/')

# information of assigned doctor and assistants, only available for admin
def control_info(request):
    if request.user.is_authenticated and request.user.is_superuser:
        doc = Doctor.objects.all()
        pat = Patient.objects.all()
        assis = Assistant.objects.all()
        newdoc = assignedDoctor.objects.all()
        newass = assignAssistant.objects.all()
        context = {"title":"Control Info","doc":doc,"pat":pat,"assis":assis,"newdoc":newdoc,"newass":newass}
        if request.method == "POST":
            if request.POST.get('assigndoctor') == "1":
                doctor = request.POST.get('doctor1')
                patient = request.POST.get('patient1')
                if doctor != "" and patient != "":
                    assigndoc = assignedDoctor(
                        patient = Patient.objects.get(pk=patient),
                        doctor = Doctor.objects.get(pk=doctor)
                    )
                    assigndoc.save()
                    return redirect('/control_info')
            elif request.POST.get('assignassistant') == "2":
                doctor = request.POST.get('doctor2')
                assistant = request.POST.get('assistant1')
                if doctor != "" and assistant != "":
                    assignassis = assignAssistant(
                        doctor = Doctor.objects.get(pk=doctor),
                        assistant = Assistant.objects.get(pk=assistant)
                    )
                    assignassis.save()
                    return redirect('/control_info')
        return render(request, 'front/control_info.html',context)
    else:
        return redirect('/')

# delete view of assigned doctor, only available for admin
def delete_assigned_doctor(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        assign_doctor = assignedDoctor.objects.filter(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            if val == "Yes":
                assign_doctor.delete()
                return redirect('/control_info')
        return render(request, 'front/delete_assigned_doctor.html')
    else:
        return redirect('/')

# delete view of assigned assistant, only available for admin
def delete_assigned_assistant(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        assign_assistant = assignAssistant.objects.filter(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            if val == "Yes":
                assign_assistant.delete()
                return redirect('/control_info')
        return render(request, 'front/delete_assigned_assistant.html')
    else:
        return redirect('/')

# medicine company view, only available for assistants
def medicine_company_add(request):
    if request.user.is_authenticated and request.user.is_assistant:
        cmp = MedicineCompany.objects.all()
        if request.method == 'POST':
            mcpy = MedicineCompany(
                company_name = request.POST.get('companyName')
            )
            mcpy.save()
            return redirect('/company')
        return render(request, 'front/add_medicine_company.html',{"title":"Add Medicine Companies","cmp":cmp})
    else:
        return redirect('/')

# edit medicine company view, only available for assistant
def edit_medicine_company(request,id):
    if request.user.is_authenticated and request.user.is_assistant:
        cmp = MedicineCompany.objects.filter(pk=id)
        if request.method == "POST":
            cmp = MedicineCompany.objects.filter(pk=id).update(company_name=request.POST.get('companyName'))
            return redirect('/company')
        return render(request, 'front/edit_medicine_company.html',{"title":"Update","cmp":cmp[0]})
    else:
        return redirect('/')

# delete medicine company view, only available for assistant
def delete_medicine_company(request, id):
    if request.user.is_authenticated and request.user.is_assistant:
        cmp = MedicineCompany.objects.filter(pk=id)
        if request.method == "POST":
            val = request.POST.get('button-value')
            cmp.delete()
            return  redirect('/company')
        return render(request, 'front/delete_medicine_company.html',{"title":"Delete","cmp":cmp[0]})
    else:
        return redirect('/')

# medicine crud view, only available for assistant
def add_medicine(request):
    if request.user.is_authenticated and request.user.is_assistant:
        med = Medicine.objects.all()
        company = MedicineCompany.objects.all()
        context = {"title":"Add Medicine","med":med,"cmp":company}
        if request.method == "POST":
            comp = request.POST.getlist('companies')
            newcomp = [int(i) for i in comp if i != None]
            medicine = Medicine(
                medicine_name = request.POST.get('medicineName'),
            )
            medicine.save()
            for i in newcomp:
                medicine.company_name.add(i)
            return redirect('/medicine')
        return render(request, 'front/add_medicine.html',context)
    else:
        return redirect('/')

# delete medicine view, only available for assistant
def delete_medicine(request, id):
    if request.user.is_authenticated and request.user.is_assistant:
        med = Medicine.objects.filter(pk=id)
        if request.method == 'POST':
            val = request.POST.get('button-value')
            med.delete()
            return redirect('/medicine')
        return render(request, 'front/delete_medicine.html',{"title":"Delete","med":med[0]})
    else:
        return redirect('/')

# prescription giving only for doctor
def give_prescription(request):
    if request.user.is_authenticated and request.user.is_doctor:
        pat = Patient.objects.all()
        med = Medicine.objects.all()
        assign = assignMedicineNew.objects.all()
        context = {"title":"Give Prescription","patient":pat,"medicine":med,'assignedMedicine':assign}
        if request.method == "POST":
            medic = request.POST.getlist('medicine')
            medic = [int(i) for i in medic if i != None]
            h,m,s = map(int, request.POST.get('time').split(":"))
            assin = assignMedicineNew(
                patient = Patient.objects.get(pk=request.POST.get('patient')),
                medicine_time = datetime.time(h,m,s)
            )
            assin.save()
            for i in medic:
                assin.medicine.add(i)
            return redirect('/give_prescription')
        return render(request, 'front/give_prescription.html',context)
    else:
        return redirect('/')


# delete prescription view only for doctor
def delete_prescribed_data(request,id):
    if request.user.is_authenticated and request.user.is_doctor:
        assin = assignMedicineNew.objects.filter(pk=id)
        if request.method == 'POST':
            val = request.POST.get('button-value')
            assin.delete()
            return redirect('/give_presciption')
        return render(request, 'front/delete_prescription.html',{"title":"Delete Prescription"})
    else:
        return redirect('/')

def patient_health(request):
    if request.user.is_authenticated and request.user.is_doctor:
        health = PatientHealthAdd.objects.all()
        context = {"title":"Health",'health':health}
        return render(request, 'front/patient_health_check.html', context)
    else:
        return redirect('/')

def delete_patient_health(request, id):
    if request.user.is_authenticated and request.user.is_doctor:
        health = PatientHealthAdd.objects.filter(pk=id)
        if request.method == 'POST':
            val = request.POST.get('button-value')
            health.delete()
            return redirect('/patient_health')
        return render(request, 'front/delete_patient_health.html',{'title':'Delete Patient Health'})
    else:
        return redirect('/')

def assign_nurse(request):
    if request.user.is_authenticated and request.user.is_doctor:
        return HttpResponse("Hello")
    else:
        return redirect('/')

def give_report(request):
    if request.user.is_authenticated and request.user.is_doctor:
        return HttpResponse("Hello")
    else:
        return redirect('/')
