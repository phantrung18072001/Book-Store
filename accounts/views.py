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

@login_required(login_url="login")
def profile(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, request.FILES ,instance=request.user)
        if form.is_valid():
            form.save()
    else: 
        form = AccountUpdateForm()
        return render(request,'user/profile.html',{'form':form})
    return render(request,'user/profile.html')

def changePass(request):
    context = {}
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        user = Account.objects.get(id=request.user.id)
        check = user.check_password(old_password)
        if check:
            if new_password1 != new_password2:
                context["Error_check3"] = "* Mật khẩu không trùng khớp"
            else:
                if len(new_password1) < 8:
                    context["Error_check2"] = "* Mật khẩu phải có ít nhất 8 ký tự"
                else:
                    user.set_password(new_password1)
                    user.save()
                    auth.authenticate(user=user.username, password=new_password1)
                    auth.login(request, user)
                    return redirect('store:home')
        else:
            context["Error_check1"] = "* Nhập sai mật khẩu"
    return render(request,'user/change_pass.html', context);