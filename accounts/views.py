from django.shortcuts import redirect, render
from django.http import HttpResponse
from accounts.forms import AccountUpdateForm, RegistrationForm
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
        if user is not None:
            auth.login(request, user)
            return redirect('store:home')
        else:
            messages.error(request,"Sai thông tin đăng nhập")
            return redirect('accounts:login')
    return render(request,'user/login.html')

def register(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_pass = form.cleaned_data['password1']
            user = auth.authenticate(username=username, password=raw_pass)
            auth.login(request, user)
            return redirect('store:home')
        else:
            context['register_form'] = form
    else:
        form = RegistrationForm()
        context['register_form'] = form
    return render(request,'user/register.html',context)

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST,instance=request.user)
        print(form)
        if form.is_valid():
            form.save()
    return render(request,'user/profile.html')
