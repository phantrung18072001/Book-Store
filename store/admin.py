from django.contrib import admin
from .models import Book, Book_Image, Book_Inventory, Cart, CartItem, Order, OrderItem


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'auth', 'category', 'price', 'country', 'year_publish')
    list_display_links = ('title',)   # Các trường có gắn link dẫn đến trang detail
    
    ordering = ('-created_at',)     # Sắp xếp theo chiều ngược
    search_fields = ('title','auth')
    # Bắt buộc phải khai báo
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class BookImageAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'path')
    list_display_links = ('book_id',)   # Các trường có gắn link dẫn đến trang detail
    # Bắt buộc phải khai báo
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
class BookInventoryAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'quantity','created_at','updated_at')
    list_display_links = ('book_id',)   # Các trường có gắn link dẫn đến trang detail
    # Bắt buộc phải khai báo
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('book', 'cart_session', 'quantity',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','address','total','status','created_at')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','book','quantity','price')


admin.site.register(Book,BookAdmin)
admin.site.register(Book_Image,BookImageAdmin)
admin.site.register(Book_Inventory,BookInventoryAdmin)

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)

