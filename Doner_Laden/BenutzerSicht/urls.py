from django.contrib import admin
from django.urls import path, include
from BenutzerSicht import views

urlpatterns = [
    #path('', views.registerUser, name='home'),
    path('', views.regTest, name='registration'),
    path('/login', views.loginValid, name='login'),
    path('/home', views.home, name='home'),
]
