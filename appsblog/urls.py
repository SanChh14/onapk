from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.appsblog, name='apps'),
    path('<int:appsblog_id>/', views.app_detail, name='app_detail'),
]
