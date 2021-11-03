from django.db import models
from django_countries.fields import CountryField
# Create your models here.

CATEGORY_CHOICES = (
    ('0','Triết học'),
    ('1','Tôn giáo'),
    ('2','Ngôn ngữ'),
    ('3','Khoa học xã hội'),
    ('4','Khoa học tự nhiên'),
    ('5','Kỹ thuật'),
    ('6','Nghệ thuật'),
    ('7','Văn học'),
    ('8','Địa lý - lịch sử'),
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    auth = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
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
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    path = models.ImageField(default="book1.jpg")

class Book_Inventory(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
