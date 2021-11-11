from django.shortcuts import render
from django.contrib import messages

from store.models import Book, Book_Inventory
# Create your views here.

def dashboard(request):
    return render(request,'admin/dashboard.html')

def book_Modify(request):
    return render(request,'admin/book_Modify.html')    

def book_Add(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('auth') and request.POST.get('category') and request.POST.get('price') and request.POST.get('publisher') and request.POST.get('country') and request.POST.get('year_publish') and request.POST.get('description') and request.POST.get('quantity') :
            newBook = Book()
            newBook_Inventory = Book_Inventory()
            newBook.title = request.POST.get('title')
            newBook.auth = request.POST.get('auth')
            newBook.category = request.POST.get('category')
            newBook.price = request.POST.get('price')
            newBook.publisher = request.POST.get('publisher')
            newBook.country = request.POST.get('country')
            newBook.year_publish = request.POST.get('year_publish')
            newBook.description = request.POST.get('description')
            newBook.save()
            newBook_Inventory.book = Book.objects.last()
            newBook_Inventory.quantity = request.POST.get('quantity')
            newBook_Inventory.save()
            messages.success(request, 'Thêm Sách mới thành công!')

    return render(request,'admin/book_Add.html')

def books_List(request):
    books_List = Book.objects.values_list('title', 'auth', 'category', 'price', 'publisher', 'country', 'year_publish')
    books_List_Inventory = Book_Inventory.objects.values_list('quantity', flat=True)
    books = zip(books_List, books_List_Inventory)
    return render(request,'admin/books_List.html',{'books': books})    

def books_Update(request):
    return render(request,'admin/books_Update.html')    

def orders_List(request):
    return render(request,'admin/orders_List.html')

def users_List(request):
    return render(request,'admin/users_List.html')    