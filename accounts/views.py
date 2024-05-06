from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib import messages

# Create your views here.
def index(req):
    return render(req, "index.html")

# signup page
def user_signup(req):
    if req.method == "POST":
        form = SignupForm(req.POST)
        print(form)
        if form.is_valid():
            # breakpoint()
            form.save()
            return redirect('accounts:login')
    else:
        form = SignupForm()
    return render(req, "signup.html", {'form':form})

# login page
def user_login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user:
                login(req, user)
                messages.success(req, "登入成功")
                return redirect('accounts:index')
            else :
                messages.error(req, "登入失敗")
    else:
        form = LoginForm()
    return render(req, "login.html", {'form':form})

# logout page
def user_logout(req):
    logout(req)
    return redirect('accounts:login')
