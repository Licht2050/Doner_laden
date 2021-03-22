from django.contrib import admin
from django.urls import path, include
from zweiteSicht import views

urlpatterns = [
    path('', views.tes_view, name='Test'),
    path('/home/', views.home, name='Home'),
    path('/roheProdukt/', views.roheProdukt, name='roheProdukt'),
    path('/benutzerSicht/', views.benutzerSicht, name='roheProdukt'),
    
    
]
