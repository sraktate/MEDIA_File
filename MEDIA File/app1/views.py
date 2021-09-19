from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from .forms import RegisterUser
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def UserRegisterView(request):
    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'app1/userRegister.html'
    context = {'form':form}
    return render(request,template_name,context)


def loginView(request):
    if request.method == 'POST':
        print('post request for login view')
        U = request.POST.get('un')
        P =request.POST.get('Pass')
        User = authenticate(username=U,password=P)
        if User is not None:
            login(request, User)
            return redirect('Home')
        else:
            messages.error(request,'Invalid Credentials!!')
    template_name = 'app1/login.html'
    context ={}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')

def HomeView(request):
    template_name = 'app1/Home.html'
    context = {}
    return render(request,template_name,context)

@login_required(login_url='login')
def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your Password was successfully Updated!')
            return redirect('login')
    teplate_name ='register/change_password.html'
    context = {'form':form}
    return render(request,teplate_name,context)
