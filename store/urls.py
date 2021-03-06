from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.home,name='home'),
    path('shelf/',views.shelf,name='shelf'),
    path('bookPage/<int:pk>',views.bookPage,name='bookPage'),
    path('infoShip',views.infoShip,name='infoShip'),
    path('add_cart/<int:book_id>/', views.add_cart, name='add_cart'),
    path('update_cart', views.update_cart, name='update_cart'),  
    path('remove_cart', views.remove_cart, name='remove_cart'),
    path('order',views.order, name='order'),
    path('update_order/<int:order_id>',views.update_order, name='update_order')
]
