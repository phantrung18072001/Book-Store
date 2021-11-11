from django.db import models
from django_countries.fields import CountryField
from django.shortcuts import reverse
from accounts.models import Account
# Create your models here.

CATEGORY_CHOICES = (
    ('Triết Học','Triết Học'),
    ('Tôn Giáo','Tôn Giáo'),
    ('Ngôn Ngữ','Ngôn Ngữ'),
    ('Khoa Học Xã Hội','Khoa Học Xã Hội'),
    ('Khoa Học Tự Nhiên','Khoa Học Tự Nhiên'),
    ('Kỹ Thuật','Kỹ Thuật'),
    ('Nghệ Thuật','Nghệ Thuật'),
    ('Văn Học','Văn Học'),
    ('Địa Lý - Lịch Sử','Địa Lý - Lịch Sử'),
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    auth = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    publisher = models.CharField(max_length=100)
    country = CountryField()
    year_publish = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table:"bookshop"

    def __str__(self):
        return self.title

class Book_Price(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE,related_name="book_price")
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Book_Image(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='images')
    main_image = models.BooleanField(default=False)
    path = models.ImageField(default="book1.jpg")

    class Meta:
        db_table:"bookshop"

class Book_Inventory(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE,related_name="inventories")
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table:"bookshop"

class Cart(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self): 
        return str(self.user) 

class CartItem(models.Model): 
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 
    cart_session = models.ForeignKey(Cart, on_delete=models.CASCADE) 
    quantity = models.IntegerField() 
    def __str__(self): 
        return str(self.book)


STATUS_ORDER = (
    ('Wait','Chờ xác nhận'),
    ('Sending','Đang vận chuyển'),
    ('Cancel','Đã hủy'),
    ('Completed','Hoàn thành')
)

class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    total = models.IntegerField()
    status = models.CharField(default=STATUS_ORDER[0][0],choices=STATUS_ORDER,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class OrderItem(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_item")
    quantity = models.IntegerField()
    price = models.IntegerField()