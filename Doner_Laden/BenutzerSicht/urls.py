from django.contrib import admin
from django.urls import path, include
from BenutzerSicht import views

urlpatterns = [
    path('', views.benutzerSicht, name='roheProdukt'),
    path('/test', views.tes_view, name='roheProdukt'),
]
