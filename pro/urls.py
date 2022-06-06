
from django.contrib import admin
from django.urls import path,include
from pro import views

urlpatterns = [
   
   path('pro/', views.pro, name='pro') 
]