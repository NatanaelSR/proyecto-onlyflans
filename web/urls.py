from django.urls import path
from . import views

urlpatterns = [
    path('', views.indice, name='indice'),
    path('acerca/', views.acerca, name='acerca'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
]