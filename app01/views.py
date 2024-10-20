from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from app01.function import *

# Create your views here.
def home(request: HttpRequest):
    return render(request, "home/home.html")

def log(request: HttpRequest):
    if request.session.get("is_login", None):
        return redirect("/dashboard/")
    
    if request.method == "GET" :
        return render(request, "home/login.html")

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

            reg_result = register(username, password)

            if reg_result == 0:
                messages.success(request, "注册成功！")
                return redirect("/login/")
            elif reg_result == 1:
                messages.error(request, "用户已存在！")
            
            return render(request, "home/login.html", locals())

def mainpage(request):
    context = {
        "user": request.user,
    }
    return render(request, "mainpage/mainpage.html", context)

def main(request):
    return render(request, "mainpage/main.html")

def publish(request):
    return render(request, "user/push.html")

def my(request):
    return render(request, "user/my.html")
