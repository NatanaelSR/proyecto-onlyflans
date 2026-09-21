from django.urls import path
from . import views

urlpatterns = [
    path('', views.indice, name='indice'),
    path('acerca/', views.acerca, name='acerca'),
    path('exito/',views.exito, name = 'exito' ),
    path('contacto/', views.contacto, name='contacto'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
]