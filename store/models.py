from django.db import models
from django_countries.fields import CountryField
from django.shortcuts import reverse
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
    price = models.IntegerField()
    publisher = models.CharField(max_length=100)
    country = CountryField()
    year_publish = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Book_Image(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='images')
    main_image = models.BooleanField(default=False)
    path = models.ImageField(default="book1.jpg")

class Book_Inventory(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="inventories")
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
