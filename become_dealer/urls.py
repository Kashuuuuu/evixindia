
from django.contrib import admin
from django.urls import path,include
from become_dealer import views

urlpatterns = [
   
   path('become_dealer/',views.become_dealer, name='become_dealer') 
]
