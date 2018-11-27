from django.contrib import admin
from .models import Postulante, Mascota, Raza ,Estado,Ciudad, Region,tipoVivienda
# Register your models here.

class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('correo', 'run', 'nombreCompleto', 'fechaNaci', 'telefono', 'Nombreregion', 'Nombreciudad', 'tipovivienda')
    search_fields = ['run','nombreCompleto']
    list_filter = ('run','nombreCompleto',)
class MascotaAdmin(admin.ModelAdmin):   
    list_display = ('nombre', 'raza', 'fechaIngreso', 'fechaNacimiento', 'Nombreestado', 'imagen')
    search_fields = ['nombre','raza']
    list_filter = ('nombre','raza',)
   

admin.site.register(Postulante,PostulanteAdmin)
admin.site.register(Mascota,MascotaAdmin)
admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Region)
admin.site.register(tipoVivienda)