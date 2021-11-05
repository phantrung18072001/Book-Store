from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from store.models import CATEGORY_CHOICES, Book, Book_Image, Book_Inventory
# Create your views here.

def home(request):
    context = {}
    categories = CATEGORY_CHOICES
    for category in categories:
        books = Book.objects.filter(category=category[0]).order_by('-created_at')[:6:1] #có 9 câu truy vấn
        if books:
            context[category[0]] = books
    return render(request,'store/home.html', {'context':context})

def shelf(request):
    return render(request,'store/shelf.html')

def bookPage(request,pk):
    book = Book.objects.get(id=pk)
    return render(request,'store/bookPage.html',{'book':book})

def infoShip(request):
    return render(request,'store/infoShip.html')

def dashboard(request):
    return render(request,'admin/dashboard.html')