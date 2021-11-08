from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.home,name='home'),
    path('shelf/',views.shelf,name='shelf'),
    path('bookPage/<int:pk>',views.bookPage,name='bookPage'),
    path('infoShip',views.infoShip,name='infoShip'),
    path('dashboard',views.dashboard,name='dashboard'),

]

""" 
    path('add_cart/<int:book_id>/', views.add_cart, name='add_cart'), 
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'), 
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
"""