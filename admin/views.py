from django.shortcuts import redirect, render
from django.db import connection
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from store.models import Book, Book_Image, Book_Inventory, Book_Price, Account, Order
from store.views import order
from django.utils import formats
# Create your views here.

def dashboard(request):
    cursor1 = connection.cursor()
    cursor1.execute("SELECT * FROM total_books;")
    total_books = cursor1.fetchall()
    cursor2 = connection.cursor()
    cursor2.execute("SELECT * FROM total_users;")
    total_users = cursor2.fetchall()
    cursor3 = connection.cursor()
    cursor3.execute("SELECT * FROM total_orders;")
    total_orders = cursor3.fetchall()
    cursor4 = connection.cursor()
    cursor4.execute("SELECT * FROM total_revenue_by_months;")
    total_revenue_by_months = cursor4.fetchall()
    cursor5 = connection.cursor()
    cursor5.execute("SELECT * FROM bestsellers;")
    bestsellers = cursor5.fetchall()
    return render(request,'admin/dashboard.html', {'total_books': total_books, 'total_users': total_users, 'total_orders': total_orders, 'total_revenue_by_months': total_revenue_by_months, 'bestsellers': bestsellers})

def statusChange(request):
    if request.user.is_admin:
        if request.method == 'POST':
            order = Order.objects.get(id=request.POST.get('orderID'))
            order.status = request.POST.get('newStatus')
            order.save()
        return redirect("adminPage:orders_List")
    return redirect('store:home')

def book_Update(request):
    if request.user.is_admin:
        if request.method == 'POST':
            if request.POST.get('title') or request.POST.get('auth') or request.POST.get('category') or request.POST.get('price') or request.POST.get('publisher') or request.POST.get('country') or request.POST.get('year_publish') or request.POST.get('description') or request.POST.get('quantity') or request.FILES.get('FrontCover_Image') or request.FILES.get('BackCover_Image'):
                newBook = Book.objects.get(id=request.POST.get('id'))
                newBook_Price = Book_Price.objects.get(book=request.POST.get('id'))
                newBook_Inventory = Book_Inventory.objects.get(book=request.POST.get('id'))
                newBook_FrontCover_Image = Book_Image.objects.get(book=request.POST.get('id'), main_image=True)
                newBook_BackCover_Image = Book_Image.objects.get(book=request.POST.get('id'), main_image=False)
                newBook.title = request.POST.get('title')
                newBook.auth = request.POST.get('auth')
                newBook.category = request.POST.get('category')
                newBook.price = request.POST.get('price')
                newBook.publisher = request.POST.get('publisher')
                newBook.country = request.POST.get('country')
                newBook.year_publish = request.POST.get('year_publish')
                newBook.description = request.POST.get('description')
                newBook.save()
                newBook_Price.price = request.POST.get('price')
                newBook_Price.save()
                newBook_Inventory.quantity = request.POST.get('quantity')
                newBook_Inventory.save()
                fs = FileSystemStorage()
                if request.FILES.get('FrontCover_Image'):
                    uploaded_FrontCover_image = request.FILES.get('FrontCover_Image')
                    newBook_FrontCover_Image.path = uploaded_FrontCover_image.name
                    fs.save(uploaded_FrontCover_image.name, uploaded_FrontCover_image)
                    newBook_FrontCover_Image.save()
                if request.FILES.get('BackCover_Image'):    
                    uploaded_BackCover_image = request.FILES.get('BackCover_Image')
                    newBook_BackCover_Image.path = uploaded_BackCover_image.name
                    fs.save(uploaded_BackCover_image.name, uploaded_BackCover_image)
                    newBook_BackCover_Image.save()         
        return redirect('adminPage:books_Update')
    return redirect('store:home')

def book_Delete(request):
    if request.user.is_admin:
        if request.method == 'POST':
            book = Book.objects.get(id=request.POST.get('id'))
            book.deleted_at = timezone.localtime(timezone.now())
            book.save()
        return redirect('adminPage:books_Update')
    return redirect('store:home')

def book_Modify(request):
    if request.user.is_admin:
        book_id = request.POST.get('bookID')
        book_Modify =  list(Book.objects.filter(id=book_id).values_list('id', 'title', 'auth', 'category', 'publisher', 'country', 'year_publish', 'description'))
        books_Modify_Inventory = list(Book_Inventory.objects.filter(book=book_id).values_list('quantity', flat=True))
        books_Modify_Price = list(Book_Price.objects.filter(book=book_id).values_list('price', flat=True))
        book_Modify_Image = list(Book_Image.objects.filter(book=book_id).values_list('path', flat=True))
        book = []
        book.append(book_Modify)
        book.append(books_Modify_Inventory)
        book.append(books_Modify_Price)
        book.append(book_Modify_Image)
        return render(request,'admin/book_Modify.html', {'book': book})
    return redirect('store:home')    

def book_Add(request):
    if request.user.is_admin:
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('auth') and request.POST.get('category') and request.POST.get('price') and request.POST.get('publisher') and request.POST.get('country') and request.POST.get('year_publish') and request.POST.get('description') and request.POST.get('quantity') and request.FILES.get('FrontCover_Image') and request.FILES.get('BackCover_Image'):
                newBook = Book()
                newBook_Price = Book_Price()
                newBook_Inventory = Book_Inventory()
                newBook_FrontCover_Image = Book_Image()
                newBook_BackCover_Image = Book_Image()
                newBook.title = request.POST.get('title')
                newBook.auth = request.POST.get('auth')
                newBook.category = request.POST.get('category')
                newBook.price = request.POST.get('price')
                newBook.publisher = request.POST.get('publisher')
                newBook.country = request.POST.get('country')
                newBook.year_publish = request.POST.get('year_publish')
                newBook.description = request.POST.get('description')
                newBook.save()
                newBook_Price.book = Book.objects.last()
                newBook_Price.price = request.POST.get('price')
                newBook_Price.save()
                newBook_Inventory.book = Book.objects.last()
                newBook_Inventory.quantity = request.POST.get('quantity')
                newBook_Inventory.save()
                uploaded_FrontCover_image = request.FILES['FrontCover_Image']
                uploaded_BackCover_image = request.FILES['BackCover_Image']
                newBook_FrontCover_Image.book = Book.objects.last()
                newBook_BackCover_Image.book = Book.objects.last()
                newBook_FrontCover_Image.main_image = True
                newBook_FrontCover_Image.path = uploaded_FrontCover_image.name
                newBook_BackCover_Image.path = uploaded_BackCover_image.name
                fs = FileSystemStorage()
                fs.save(uploaded_FrontCover_image.name, uploaded_FrontCover_image)
                fs.save(uploaded_BackCover_image.name, uploaded_BackCover_image)
                newBook_FrontCover_Image.save()
                newBook_BackCover_Image.save()
                messages.success(request, 'Thêm sách thành công!')
            else:
                messages.error(request, 'Thêm sách thất bại! Bạn phải điền đầy đủ thông tin!')
            return render(request,'admin/book_Add.html')
        else:
            return render(request,'admin/book_Add.html')
    return redirect('store:home')    

def books_List(request):
    if request.user.is_admin:
        books_List = list(Book.objects.filter(deleted_at = None).values_list('title', 'auth', 'category', 'publisher', 'country', 'year_publish'))
        books_List_Inventory = list(Book_Inventory.objects.values_list('quantity', flat=True))
        books_List_Price = list(Book_Price.objects.values_list('price', flat=True))
        books = []
        for x in range(len(books_List)):
            book = []
            book.append(x + 1)
            book.extend(books_List[x])
            book.append("{:,} VNĐ".format(books_List_Price[x]).replace(',','.'))
            book.append(books_List_Inventory[x])
            books.append(book)
        return render(request,'admin/books_List.html',{'books': books})    
    return redirect('store:home')    

def books_Update(request):
    if request.user.is_admin:
        books_List = list(Book.objects.filter(deleted_at = None).values_list('id', 'title', 'auth', 'category', 'year_publish'))
        books_List_Inventory = list(Book_Inventory.objects.values_list('quantity', flat=True))
        books_List_Price = list(Book_Price.objects.values_list('price', flat=True))
        books = []
        for x in range(len(books_List)):
            book = []
            book.append(x + 1)
            book.extend(books_List[x])
            book.append("{:,} VNĐ".format(books_List_Price[x]).replace(',','.'))
            book.append(books_List_Inventory[x])
            books.append(book)
        return render(request,'admin/books_Update.html',{'books': books})    
    return redirect('store:home')    

def orders_List(request):
    if request.user.is_admin:
        cursor1 = connection.cursor()
        cursor1.execute("SELECT BSO.id, BAA.username, BSO.address, BSO.total, BSO.status, BSO.created_at, BSO.updated_at FROM bookshop.store_order BSO JOIN bookshop.accounts_account BAA ON BSO.user_id = BAA.id ORDER BY BSO.created_at DESC;")
        orders_List = cursor1.fetchall()
        cursor2 = connection.cursor()
        cursor2.execute("SELECT BSO.order_id, BSB.title, BSO.quantity FROM bookshop.store_book BSB JOIN bookshop.store_orderitem BSO ON BSO.book_id = BSB.id")
        orders_List_Books = cursor2.fetchall()
        orders_Books = []
        for x in range(len(orders_List)):
            order = ""
            for y in range(len(orders_List_Books)):
                if orders_List[x][0] == orders_List_Books[y][0]:
                    order = order  + orders_List_Books[y][1] + " x" + str(orders_List_Books[y][2]) + "\n"
                elif orders_List[x][0] < orders_List_Books[y][0]:
                    break
            orders_Books.append(order)
        orders_Info = []
        for x in range(len(orders_List)):
            order_Info = []
            order_Info.append(x + 1)
            order_Info.append(orders_List[x][0])
            order_Info.append(orders_List[x][1])
            order_Info.append(orders_Books[x])
            order_Info.append("{:,} VNĐ".format(orders_List[x][3]).replace(',','.'))
            order_Info.append(formats.date_format(orders_List[x][5], "SHORT_DATETIME_FORMAT"))
            if orders_List[x][4] != "Hoàn thành":
                order_Info.append("Chưa rõ")
            else:
                order_Info.append(formats.date_format(orders_List[x][6], "SHORT_DATETIME_FORMAT"))
            order_Info.append(orders_List[x][2])
            buttonContent = ["Chờ xử lý", "Đang vận chuyển", "Hoàn thành", "Đã hủy"]
            content = orders_List[x][4]
            buttonContent.remove(content)
            buttonContent.insert(0, content)
            order_Info.append(buttonContent)
            orders_Info.append(order_Info)
        return render(request,'admin/orders_List.html',{'orders_Info': orders_Info})
    return redirect('store:home')    

def users_List(request):
    if request.user.is_admin:
        users_List = list(Account.objects.values_list('username', 'email', 'phone', 'address'))
        users = []
        for x in range(len(users_List)):
            user = []
            user.append(x + 1)
            user.extend(users_List[x])
            users.append(user)
        return render(request,'admin/users_List.html',{'users': users})    
    return redirect('store:home')    
