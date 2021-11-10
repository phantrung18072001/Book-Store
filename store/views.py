from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage

from store.models import CATEGORY_CHOICES, Book, Cart, CartItem
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

def add_cart(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            book_quantity = int(request.POST.get('quantity'))
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user)

        is_exist_cart_item = CartItem.objects.filter(cart_session=cart,book=book).exists()
        if is_exist_cart_item:
            pass
        else:
            cart_item = CartItem.objects.create(cart_session=cart, book=book, quantity=book_quantity)
            cart.total += book_quantity * book.price;
            cart_item.save()
            cart.save()
        return redirect(request.META['HTTP_REFERER'])

def update_cart(request):
    if request.method == 'POST':    
        if request.user.is_authenticated:
            cartitem_id = int(request.POST.get('cartitem_id'))
            cart_item_quantity = int(request.POST.get('quantity'))
            cart_item = CartItem.objects.get(id=cartitem_id)

            old_quantity = cart_item.quantity
            cart_item.quantity = cart_item_quantity
            cart_item.save()
            cart = Cart.objects.get(id=cart_item.cart_session.id)
            cart.total = cart.total + (cart_item.quantity-old_quantity) * cart_item.book.price
            cart.save()
            return JsonResponse({'status':'Update successfully','total_cart':cart.total})
        else:
            return JsonResponse({'status':'Back to login'})
    return redirect("/")

def remove_cart(request):
    if request.method == 'POST':    
        if request.user.is_authenticated:
            cartitem_id = int(request.POST.get('cartitem_id'))
            count = int(request.POST.get('count'))
            count -= 1
            cart_item = CartItem.objects.get(id=cartitem_id)
            cart = Cart.objects.get(id=cart_item.cart_session.id)
            cart.total = cart.total - cart_item.quantity * cart_item.book.price
            cart_item.delete()
            cart.save()
            return JsonResponse({'status':'Update successfully','total_cart':cart.total, 'count':count})
        else:
            return JsonResponse({'status':'Back to login'})
    return redirect("/")


def infoShip(request):
    return render(request,'store/infoShip.html')

def dashboard(request):
    return render(request,'admin/dashboard.html')