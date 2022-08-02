from django.urls import re_path as url
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
app_name = "tikets"

urlpatterns = [
    path(r'tikets', views.TiketsList.as_view()),
    path(r'tikets/<int:pk>/', views.TiketsDetail.as_view()),
    path(r'topic', views.TopicView.as_view()),
    path(r'users', views.UserView.as_view()),
    path(r'users/<str:username>', views.UserDetail.as_view()),
    path(r'user/<int:pk>', views.UserNameID.as_view()),
    path(r'inplemention', views.InplementionView.as_view()),
    path(r'send_user_ajax/', views.send_user_ajax),
    path(r'tikets_id/', views.tiket_id.as_view()),


]