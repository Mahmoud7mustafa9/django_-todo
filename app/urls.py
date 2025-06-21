from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Home , name= "home"),
    path('update/<str:pk>/', views.update_task , name= "update"),
    path('delete/<str:pk>/', views.delete_task , name= "delete"),
]