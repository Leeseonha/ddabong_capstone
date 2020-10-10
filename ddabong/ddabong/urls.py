"""ddabong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
import theme.views
import contact.views
import items.views
import mypage.views
import voulunteer_work.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('oauth/', account.views.oauth, name='oauth'),
    # path('account/login/kakao/', account.views.kakao_login, name='kakao_login'),
    path('account/login/kakao/callback/', account.views.KakaoLoginVIew, name='KakaoLoginVIew'),
    path('', include('theme.urls')),
    path('v_area/',  voulunteer_work.views.v_area, name='v_area'),
    path('v_detail/',  voulunteer_work.views.v_detail, name='v_detail'),
    path('mypage/',  mypage.views.mypage, name='mypage'),
    path('items/', items.views.items, name='items'),
    path('keyboard/', items.views.keyboard, name='keyboard'),
    path('message/', items.views.message, name='message'),
]
