#from django.conf.urls import url
from django.urls import include, re_path
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
app_name = "ajax_tikets"

urlpatterns = [
    re_path(r'/hello/', views.hello),
    #url(r'^home/', 'myapp.views.home'),


]