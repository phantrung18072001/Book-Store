from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.home,name='home'),
    path('shelf',views.shelf,name='shelf'),
    path('bookPage/<int:pk>',views.bookPage,name='bookPage'),
    path('infoShip',views.infoShip,name='infoShip'),
    path('dashboard',views.dashboard,name='dashboard'),
]