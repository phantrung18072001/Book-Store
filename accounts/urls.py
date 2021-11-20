from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout', views.logout, name='logout'),
    path('profile',views.profile, name='profile'),
    path('changePass',views.changePass, name='changePass'),
]