from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views as auth_views   # 로그인/로그아웃 커스터마이징
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lecture/', views.lecture_note, name='lecture_note'),


    path('accounts/',include('django.contrib.auth.urls')),


    # 로그아웃, 로그인 커스터마이징
    # # path('logout', auth_views.auth_logout,name='logout',),
    # path('login', auth_views.auth_login,{'template_name':'registration/login.html'},name='login'),
    # path('logout', auth_logout, name='logout'),



    path('accounts/signup', views.CreateUserView.as_view(), name = 'signup'),
    path('accounts/login/done', views.RegisteredView.as_view(), name = 'create_user_done'),

    path('home/contact', views.contact, name='contact')

]
