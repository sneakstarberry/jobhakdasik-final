from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('mypage/', views.mypage, name="mypage"),
    path('change/', views.change, name="change"),
    
]