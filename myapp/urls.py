from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('game_1/', views.index, name='game_1'),
    path('game_2/', views.index, name='game_2'),
    path('game_3/', views.index, name='game_3'),

]
