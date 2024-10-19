from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from function import *

# Create your views here.
def home(request: HttpRequest):
    return render(request, "home/home.html")

def log(request: HttpRequest):
    if request.session.get("is_login", None):
        return redirect("/dashboard/")

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        register_form = RegisterForm(request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data["log_username"]
            password = login_form.cleaned_data["log_password"]

            login_result = login(username, password)

            if login_result == 0:
                request.session["is_login"] = True
                request.session["user_id"] = username
                return redirect("/dashboard/")
            elif login_result == 1:
                messages.error(request, "密码错误！")
            elif login_result == 2:
                messages.error(request, "用户不存在！")

            return render(request, "home/login.html", locals())
        
        elif register_form.is_valid():
            username = register_form.cleaned_data["reg_username"]
            email = register_form.cleaned_data["reg_email"]
            password = register_form.cleaned_data["reg_password"]
            password2 = register_form.cleaned_data["reg_password2"]
            
    return render(request, "home/login.html")

def mainpage(request):
    context = {
        "user": request.user,
    }
    return render(request, "mainpage/mainpage.html", context)
