from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    #path('', views.get_name, name='get_name'),
    #path('', views.main),
    path('', views.index),
    path('index', views.index),
    path('create/', views.create),
    #path('app/', views.bar),
    path('tiketsList/', views.tiketsList),
    path('startbot/', views.start_bot),
    path('stopbot/', views.stop_bot),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='tikets/login.html')),
    #path('accounts/login/', auth_views.LoginView.as_view(template_name='tikets/tiketsList.html')),
    ##path('accounts/logout/', auth_views.LogoutView.as_view(template_name='tikets/logout.html')),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='tikets/index.html')),

]