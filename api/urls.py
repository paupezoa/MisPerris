from django.urls import path
from .views import agregar_mascota,listar_mascotas,eliminar_mascota,modificar_mascota,agregar_token

urlpatterns = [
    path('agregar_mascota/', agregar_mascota, name="api_agregar_mascota"),
    path('listar_mascotas/', listar_mascotas, name="api_listar_mascotas"),
    path('eliminar_mascota/<id>/', eliminar_mascota, name="api_eliminar_mascota"),
    path('modificar_mascota/', modificar_mascota, name="api_modificar_mascota"),
    path('agregar-token/',agregar_token, name="api_agregar_token"),
]