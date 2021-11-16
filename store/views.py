from django.db import connection
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage

from store.models import CATEGORY_CHOICES, Book, Cart, CartItem, Order, OrderItem
# Create your views here.

def home(request):
    context = {}
    categories = CATEGORY_CHOICES
    for category in categories:
        books = Book.objects.filter(category=category[0],deleted_at=None).prefetch_related('inventories','images').order_by('-created_at')[:6:1] #có 9 câu truy vấn
        if books:
            context[category[0]] = books
    return render(request,'store/home.html', {'context':context})

def shelf(request):
    info = request.GET.get('info',"")
    choose = request.GET.get('choose',"")
    category = request.GET.get('category',"")
    cursor = connection.cursor()
    books = None
    #search in user
    if info is not None and info.strip() != '':
        cursor.execute('call search_by_info("%s","%s")'%(info, choose))
        books = cursor.fetchall()[::-1]
    elif category:
        cursor.execute('call search_by_category("%s")'%(category))
        books = cursor.fetchall()[::-1]
    else:
        return redirect(request.META['HTTP_REFERER'])
    # search in admin
    if request.is_ajax():
        return JsonResponse({'status':"success", 'books':books})
    return render(request,'store/shelf.html',{'books':books, 'category':category, 'info':info})

def bookPage(request,pk):
    book = Book.objects.filter(id=pk).prefetch_related('inventories','images')[0]
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
                cart.total += book_quantity * book.book_price.price;
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
            cart.total = cart.total + (cart_item.quantity-old_quantity) * cart_item.book.book_price.price
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
            cart.total = cart.total - cart_item.quantity * cart_item.book.book_price.price
            cart_item.delete()
            cart.save()
            return JsonResponse({'status':'Update successfully','total_cart':cart.total, 'count':count})
        else:
            return JsonResponse({'status':'Back to login'})
    return redirect("/")

def order(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart_session=cart)
    if request.method == 'POST':
        address = request.POST.get('address')

        for cart_item in cart_items:
            if cart_item.book.inventories.quantity < cart_item.quantity:
                messages.error(request,'Vượt quá số lượng sách %s còn lại trong kho'%cart_item.book)
                return redirect(request.META['HTTP_REFERER'])

        order = Order.objects.create(user=user, address=address, total=cart.total)
        for cart_item in cart_items:
            cart_item.book.inventories.quantity -= cart_item.quantity
            cart_item.book.inventories.save()
            orderitem = OrderItem.objects.create(order=order,book=cart_item.book,
                                    quantity=cart_item.quantity,price=cart_item.book.book_price.price)
        cart_items.delete()
        cart.delete()
    return redirect("store:infoShip")

def update_order(request,order_id):
    order = Order.objects.get(id=order_id)
    order.status = "Đã hủy"
    order.save()
    return redirect("store:infoShip")

def infoShip(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-created_at')
    return render(request,'store/infoShip.html',{'orders':orders})

def dashboard(request):
    return redirect("adminPage:books_List")