from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'store/home.html')

def shelf(request):
    return render(request,'store/shefl.html')

def bookPage(request):
    return render(request,'store/bookPage.html')

def profile(request):
    return render(request,'store/profile.html')

def infoShip(request):
    return render(request,'store/infoShip.html')

def dashboard(request):
    return render(request,'admin/dashboard.html')