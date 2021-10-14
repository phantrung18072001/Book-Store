from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('shelf',views.shelf,name='shelf'),
    path('bookPage',views.bookPage,name='bookPage'),
    path('profile',views.profile,name='profile'),
    path('infoShip',views.infoShip,name='infoShip'),
    path('dashboard',views.dashboard,name='dashboard'),
]