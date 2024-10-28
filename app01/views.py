import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from app01.function import *
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request: HttpRequest):
    request.session["is_login"] = False
    request.session["user_name"] = None
    return render(request, "home/home.html")


def log(request: HttpRequest):
    if request.session.get("is_login", None):
        return redirect("/dashboard/")

    if request.method == "GET":
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
                request.session["user_name"] = username
                return redirect("/dashboard/")
            elif login_result == 1:
                messages.error(request, "密码错误！")
            elif login_result == -1:
                messages.error(request, "用户不存在！")

            return render(request, "home/login.html", locals())

        elif register_form.is_valid():
            username = register_form.cleaned_data["reg_username"]
            # email = register_form.cleaned_data["reg_email"]
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
    user_info = check_user(request.session.get("user_name", None))
    context = {
        "login_result": request.session.get("is_login", None),
        "image_url": user_info.image,
    }
    return render(request, "mainpage/mainpage.html", context)


def dashboard_recommend(request):
    return render(request, "mainpage/waterfallshowcard/recommend.html")


def get_recommend_notice(request):
    notice_list = check_all_notice()

    if not notice_list:
        serialize_notice_list = []
    else:
        serialize_notice_list = [serialize_notice(notice) for notice in notice_list]
    return JsonResponse({"notice_list": serialize_notice_list}, safe=False)


def dashboard_sports(request):
    return render(request, "mainpage/waterfallshowcard/sports.html")


def dashboard_emotion(request):
    return render(request, "mainpage/waterfallshowcard/emotion.html")


def dashboard_food(request):
    return render(request, "mainpage/waterfallshowcard/food.html")


def dashboard_study(request):
    return render(request, "mainpage/waterfallshowcard/study.html")


def dashboard_travel(request):
    return render(request, "mainpage/waterfallshowcard/travel.html")


def dashboard_games(request):
    return render(request, "mainpage/waterfallshowcard/games.html")


def main(request, post_id):
    post = check_notice(post_id)
    author = check_notice_owner(post.owner_id)
    context = {
        "post": post,
        "author": author,
    }
    return render(request, "mainpage/main.html", context)


def yinsixieyi(request):
    return render(request, "mainpage/yinsixieyi.html")


def kefu(request):
    return render(request, "mainpage/kefu.html")


def my(request):
    if request.method == "GET":
        if request.session.get("is_login", None):
            username = request.session["user_name"]
            user_info = check_user(username)
            if user_info.introduction == "unknown":
                user_info.introduction = "这个人还没有个人介绍"
            context = {
                "user_nickname": user_info.nickname,
                "user_introduction": user_info.introduction,
                "user_avatar": user_info.image,
                "user_id": user_info.id,
            }
            return render(request, "user/my.html", context)
        else:
            messages.error(request, "请先登录！")
            return redirect("/login/")


def change_username(request):
    if request.method == "POST":
        new_nickname = request.POST.get("username")
        username = request.session["user_name"]

        user_info = check_user(username)
        old_nickname = user_info.nickname

        if new_nickname == old_nickname:
            messages.error(request, "新昵称不能与旧昵称相同！")
            return redirect("/my/")

        if len(new_nickname) > 10:
            messages.error(request, "昵称长度不能超过10个字符！")
            return redirect("/my/")

        user_info.nickname = new_nickname
        result = change_user_info(user_info)
        if result == 0:
            messages.success(request, "修改成功！")
            return redirect("/my/")
        else:
            messages.error(request, "修改失败！")
            return redirect("/my/")

    return render(request, "user/myoptions/mychangeinfo.html")


def change_desc(request):
    if request.method == "POST":
        new_desc = request.POST.get("desc")
        username = request.session["user_name"]

        if new_desc == "":
            messages.error(request, "个人介绍不能为空！")
            return redirect("/my/")

        user_info = check_user(username)
        user_info.introduction = new_desc
        result = change_user_info(user_info)

        if result == 0:
            messages.success(request, "修改成功！")
            return redirect("/my/")
        else:
            messages.error(request, "修改失败！")
            return redirect("/my/")

    return render(request, "user/myoptions/mychangeinfo.html")


def change__password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        username = request.session["user_name"]

        if not re.match(r"^[a-zA-Z0-9]{6,18}$", new_password):
            messages.error(request, "密码必须为6-18位字母或数字！")
            return redirect("/my/")

        if old_password == new_password:
            messages.error(request, "新密码不能与旧密码相同！")
            return redirect("/my/")

        result = change_password(username, old_password, new_password)

        if result == 0:
            messages.success(request, "修改成功！")
            return redirect("/my/")
        elif result == 1:
            messages.error(request, "旧密码错误！")
            return redirect("/my/")

    return render(request, "user/myoptions/mychangeinfo.html")


def change_avatar(request):
    if request.method == "POST":
        image_url = request.POST.get("image_url")
        username = request.session["user_name"]

        if image_url == "":
            messages.error(request, "请先上传图片！")
            return redirect("/my/")

        user_info = check_user(username)
        user_info.image = image_url
        result = change_user_info(user_info)

        if result == 0:
            messages.success(request, "修改成功！")
            return redirect("/my/")
        else:
            messages.error(request, "修改失败！")
            return redirect("/my/")

    return render(request, "user/myoptions/mychangeinfo.html")


def published(request):
    return render(request, "user/myoptions/mypublished.html")

def get_my_published_notice(request):
    notice_list = check_my_notice(request.session.get("user_name", None))
    if not notice_list:
        serialize_notice_list = []
    else:
        serialize_notice_list = [serialize_notice(notice) for notice in notice_list]
    return JsonResponse({"notice_list": serialize_notice_list}, safe=False)


@csrf_exempt
def publish(request):
    if not request.session.get("is_login", None):
        return redirect("/dashboard/")  # 如果未登录，重定向到仪表盘

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))

            title = data.get("title", "unknown")  # 默认值为"unknown"
            contact = data.get("contact")
            content = data.get("content")
            category = data.get("category", 0)  # 默认值为0
            tags = data.get("tags") if data.get("tags") else []  # 确保 tags 是一个列表
            image_url = data.get("imageUrl")
            current_date = data.get("date", "unknown")  # 默认值为"unknown"
            notice_id = add_notice(
                request.session["user_name"]
            )  # 传入当前用户名或用户ID
            # print(notice_id)
            if notice_id == -1:
                return JsonResponse({"error": "用户不存在"}, status=400)

            notice = check_notice(notice_id)
            if notice is None:
                return JsonResponse({"error": "获取通知失败"}, status=400)

            notice.owner_contact = contact
            notice.title = title
            notice.basic_type = category
            notice.image = image_url
            notice.time = current_date
            notice.description = content
            notice.tag_list = tags

            if change_notice(notice) == -1:
                return JsonResponse({"error": "更新通知失败"}, status=400)

            return JsonResponse({"message": "发布成功"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "发布失败，数据格式错误"}, status=400)

    return render(request, "user/push.html")


def replied(request):
    return render(request, "user/myoptions/myreplied.html")

def get_my_replied_notice(request):
    notice_list = check_request_notice(request.session.get("user_name", None))
    if not notice_list:
        serialize_notice_list = []
    else:
        serialize_notice_list = [serialize_notice(notice) for notice in notice_list]
    return JsonResponse({"notice_list": serialize_notice_list}, safe=False)


def info(request):
    return render(request, "user/myoptions/mychangeinfo.html")


def message(request):
    return render(request, "user/message.html")
