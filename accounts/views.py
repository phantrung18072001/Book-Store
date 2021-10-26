from django.shortcuts import redirect, render
from django.http import HttpResponse
from accounts.models import Account
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required 
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request=request, message="Login successful!")
            return redirect('store:home')
        else:
            messages.error(request,"Sai thông tin đăng nhập")
            return redirect('accounts:login')
    return render(request,'user/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        phone = request.POST['phone']
        email = request.POST['email']
        birth = request.POST['birth']
        address = request.POST['address']
        if pass1 == pass2:
            myuser = Account.objects.create_user(name=name,username=username,phone=phone,email=email,password=pass1)
            if birth is not None:
                myuser.birth = birth
            if address is not None:
                myuser.address = address
            myuser.save()
            messages.success(request,"Đăng ký thành công!")
            return redirect('accounts:login')
    else:
        return render(request,'user/register.html')

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    messages.success(request=request, message="You are logged out!")
    return redirect('accounts:login')