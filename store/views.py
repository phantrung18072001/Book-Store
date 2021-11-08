from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage

from store.models import CATEGORY_CHOICES, Book
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
    info = request.GET.get('info',"")
    choose = request.GET.get('choose',"")
    category = request.GET.get('category',"")
    books = None
    if info is not None and info.strip() != '':
        if choose == 'title':
            books = Book.objects.filter(title__icontains=info).order_by('-created_at')
        elif choose == 'auth':
            books = Book.objects.filter(auth__icontains=info).order_by('-created_at')
    elif category:
        books = Book.objects.filter(category=category).order_by('-created_at')
    else:
        return redirect(request.META['HTTP_REFERER'])
    p = Paginator(books, 1)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request,'store/shelf.html',{'books':page, 'category':category, 'info':info, 'paginator':p})

def bookPage(request,pk):
    book = Book.objects.get(id=pk)
    return render(request,'store/bookPage.html',{'book':book})
    

def infoShip(request):
    return render(request,'store/infoShip.html')

def dashboard(request):
    return render(request,'admin/dashboard.html')