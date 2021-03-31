from django.contrib import admin
from django.urls import path, include
from BenutzerSicht import views

urlpatterns = [

    path('/home', views.HomeView.as_view(), name='home'),
    path('/login', views.loginUser, name='login'),
    path('/logout', views.logoutUser, name='logout'),
    path('/registration', views.registerUser, name='registration'),
    path('/home/<int:id>', views.RemoveFromCard, name='home'),
    
    
]