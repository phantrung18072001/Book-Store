from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from store.models import Book
# Create your views here.

def home(request):
    context = {}
    books = Book.objects.all()
    return render(request,'store/home.html')

def shelf(request):
    return render(request,'store/shelf.html')

def bookPage(request):
    return render(request,'store/bookPage.html')

def infoShip(request):
    return render(request,'store/infoShip.html')

def dashboard(request):
    return render(request,'admin/dashboard.html')