from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"title":"Home"}
    return render(request,'front/home.html',context)

def about(request):
    context = {"title":"About"}
    return render(request,'front/about.html',context)