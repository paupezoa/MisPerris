from django.urls import path
from .views import home, formulario, agregar_mascota,listar_mascotas,eliminar_mascotas,modificar_mascota,servicios

urlpatterns = [
    path('',home,name="home"),
    path('formulario/', formulario, name="formulario"),
    path('agregar_mascota/', agregar_mascota, name="agregar_mascota"),
    path('listar_mascotas/', listar_mascotas, name="listar_mascotas"),
    path('eliminar_mascotas/<id>/', eliminar_mascotas, name="eliminar_mascotas"),
    path('modificar_mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('servicios/',servicios, name="servicios"),
]