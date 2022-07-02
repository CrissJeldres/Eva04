from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
path('', index, name="index"),
path('perro', perro, name="perro"),
path('gatos', gatos, name="gatos"),
path('aves', aves, name="aves"),
path('descuentos', descuentos, name="descuentos"),
path('suscribirse', suscribirse, name="suscribirse"),
path('productos', productos, name="productos"),
path('carrito', carrito, name="carrito"),
path('inicio', inicio, name="inicio"),
path('crear', crear, name="crear"),
path('compras', compras, name="compras"),
path('agregar', agregar, name="agregar"),
path('crearproducto', crearproducto, name="crearproducto"),
path('eliminarproducto/<id>', eliminarproducto, name="eliminarproducto"),
path('modificar/<id>', modificar, name="modificar"),
path('pagar', pagar, name="pagar"),
path('cancelar/<id>', cancelar, name="cancelar"),
path('modificarcompra/<id>', modificarcompra, name="modificarcompra"),
path('registro', registro, name="registro"),

]



