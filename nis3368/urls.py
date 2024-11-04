"""
URL configuration for nis3368 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from app01 import views
from django.conf import settings
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("", views.home),
    path("home/", views.home),
    path("login/", views.log),
    path('logout/', views.logout, name='logout'),
    path("dashboard/", views.mainpage),
    path("dashboard/recommend/", views.dashboard_recommend),
    path("dashboard/sports/", views.dashboard_sports),
    path("dashboard/emotion/", views.dashboard_emotion),
    path("dashboard/food/", views.dashboard_food),
    path("dashboard/study/", views.dashboard_study),
    path("dashboard/travel/", views.dashboard_travel),
    path("dashboard/games/", views.dashboard_games),
    path("dashboard/search/", views.search, name="search"),
    path("main/<int:post_id>/", views.main),
    path("publish/", views.publish, name="publish"),
    path("my/<int:user_id>/", views.my),
    path("my/published/", views.published),
    path("my/replied/", views.replied),
    path("my/info/", views.info),
    path("message/", views.message),
    path("yinsixieyi/", views.yinsixieyi),
    path("kefu/", views.kefu),
    path("change_username/", views.change_username, name="change_username"),
    path("change_desc/", views.change_desc, name="change_desc"),
    path("change_avatar/", views.change_avatar, name="change_avatar"),
    path("change_password/", views.change__password, name="change_password"),
    path("get-recommend-notice/", views.get_recommend_notice),
    path("get-sports-notice/", views.get_sports_notice),
    path("get-emotion-notice/", views.get_emotion_notice),
    path("get-food-notice/", views.get_food_notice),
    path("get-study-notice/", views.get_study_notice),
    path("get-travel-notice/", views.get_travel_notice),
    path("get-games-notice/", views.get_games_notice),
    path("get-search-notice/", views.get_search_notice, name="get_search_notice"),
    path("get-my-published-notice/", views.get_my_published_notice),
    path("get-my-replied-notice/", views.get_my_replied_notice),
    path("api/request_notice", views.request_notice_view, name="request_notice"),
    # path("applylist/<int:post_id>/", views.applylist, name="applylist"),
    path("answer_request/", views.handle_answer_request, name="answer_request"),

    path("api/disable_notice", views.disable__notice),
    path("api/recover_notice", views.recover_notice),
    path("applylist/<int:post_id>/", views.applylist, name="applylist"),
]
