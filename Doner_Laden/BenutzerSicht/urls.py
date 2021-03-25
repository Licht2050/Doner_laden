from django.contrib import admin
from django.urls import path, include
from BenutzerSicht import views

urlpatterns = [
    # path('', views.registerUser, name='home'),
    # path('', views.regTest, name='registration'),

    path('/', views.home, name='home'),
    path('/login', views.loginUser, name='login'),
    path('/registration', views.registerUser, name='registration'),
]
