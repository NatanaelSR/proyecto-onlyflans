from django.urls import path
from . import views

urlpatterns = [

    path('', views.indice, name='indice'),
    path('acerca/', views.acerca, name='acerca'),
    path('exito/', views.exito, name='exito'),
    path('login/',views.log_in, name = 'login'),
    path('signup/',views.sign_up, name = 'signup'),
    path('contacto/', views.contacto, name='contacto'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('flan/<int:flan_id>/', views.flan_detail, name='flan_detalle'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:flan_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('logout/',views.log_out,name='logout')
]
