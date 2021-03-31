from django.contrib import admin
from django.urls import path, include
from MitarbeiterSicht import views

urlpatterns = [
    # path('', views.registerUser, name='home'),
    # path('', views.regTest, name='registration'),

    path('', views.staffView, name='homeMitarbeiterSicht'),
    path('/orders', views.Orders, name='orders'),
    path('/statistic', views.Statistic, name='statistic'),
    path('/messages', views.Messages, name='messages'),
    path('/resources', views.Resources, name='resources')
]