
from django.contrib import admin
from django.urls import path,include
from dashboard import views

urlpatterns = [
   
   path('',views.admin_dash, name='admin_dash'),
   path('login/',views.admin_login, name='login'),
   path('ad_logout',views.ad_logout, name='ad_logout'),
   path('admin_profile',views.admin_profile, name='admin_profile'),
   path('password_reset',views.password_reset, name='password_reset'),
   path('user',views.user, name='user'),
   path('dealer',views.dealer, name='dealer'),

]