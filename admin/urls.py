from django.urls import path
from . import views

app_name = 'admin'

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('book_Modify',views.book_Modify,name='book_Modify'),
    path('book_Add',views.book_Add,name='book_Add'),
    path('books_List',views.books_List,name='books_List'),
    path('books_Update',views.books_Update,name='books_Update'),
    path('orders_List',views.orders_List,name='orders_List'),
    path('users_List',views.users_List,name='users_List'),
]