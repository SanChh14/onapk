from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gamesblog, name='games'),
    path('<int:gamesblog_id>/', views.game_detail, name='game_detail'),

]
