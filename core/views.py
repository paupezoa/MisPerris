from django.shortcuts import render,redirect
from .models import Postulante, Mascota , Region , Ciudad , tipoVivienda ,Estado, Raza
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from fcm_django.models import FCMDevice


def home(request):
    return render(request, 'core/home.html')

def formulario(request):
    tipoviv = tipoVivienda.objects.all()
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    variables = {
        'tipoviv':tipoviv,
        'regiones':regiones,
        'ciudades':ciudades
    }

    
    # el ultimo sobreescribe a las otras variables
    
    if request.POST:
        pos = Postulante()
        pos.correo = request.POST.get('txtCorreo')
        pos.run = request.POST.get('txtRut')
        pos.nombreCompleto = request.POST.get('txtNombre')
        pos.fechaNaci = request.POST.get('txtFecha')
        pos.telefono = request.POST.get('txtFono')
        
        region = Region()
        region.id = request.POST.get('cboRegion')
        pos.Nombreregion = region

        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        pos.Nombreciudad = ciudad

        tpvivienda = tipoVivienda()
        tpvivienda.id = request.POST.get('cboTipoVivienda')
        pos.tipovivienda = tpvivienda

        try:
            pos.save()
            messages.success(request, 'Guardado Correctamente')
        except:
            messages.error(request, 'No se ha podido Guardar') 
            return redirect('formulario')  
    return render(request, 'core/formulario.html', variables)

@login_required
def agregar_mascota(request):
    razas = Raza.objects.all()
    estados = Estado.objects.all()
    variables = {
        'razas':razas,
        'estados':estados
     }
    
    if request.POST:
        mas = Mascota()
        mas.nombre = request.POST.get('txtNombreMas')
        
        raz =   Raza()
        raz.id = request.POST.get('cboRaza')
        mas.raza = raz

        mas.genero = request.POST.get('txtGenero')
        mas.fechaIngreso = request.POST.get('txtFechaIn')
        mas.fechaNacimiento = request.POST.get('txtFechaNa')

        est =   Estado()
        est.id = request.POST.get('cboEstado')
        mas.Nombreestado = est

        mas.imagen = request.FILES.get('imagen')

        try:
            mas.save()
            messages.success(request, 'Guardado Correctamente')
        except:
            messages.error(request, 'No se ha podido Guardar') 
            return redirect('listar_mascotas')  
    return render(request, 'core/agregar_mascota.html', variables)


@login_required
def listar_mascotas(request):
     masco = Mascota.objects.all()
     variables = {
        'masco':masco
     }
     return render(request,'core/listar_mascotas.html',variables)
    

@login_required
def eliminar_mascotas(request,id):
     masco = Mascota.objects.get(id=id)
     try:
         masco.delete()
         messages.success(request, 'Eliminado Correctamente')
     except:
        messages.error(request, 'No se ha podido Eliminar') 
    
     return redirect('listar_mascotas')  

@login_required
def modificar_mascota(request, id):
        masco = Mascota.objects.get(id=id)
        razas = Raza.objects.all()
        estados = Estado.objects.all()
        
        variables = {
            'masco':masco,
            'razas':razas,
            'estados':estados
        }

        if request.POST:
            mascota = Mascota()
            mascota.id = request.POST.get('txtId')
            mascota.nombre = request.POST.get('txtNombreMascota')
            
            raz =   Raza()
            raz.id = request.POST.get('cboRaza')
            mascota.raza = raz

            mascota.genero = request.POST.get('txtGenero')
            mascota.fechaIngreso = request.POST.get('txtFechaIn')
            mascota.fechaNacimiento = request.POST.get('txtFechaNa')

            est =   Estado()
            est.id = request.POST.get('cboEstado')
            mascota.Nombreestado = est

            mascota.imagen = request.POST.get('imagen')

            
            try:
                mascota.save()
                messages.success(request, 'Modificado Correctamente')
            except:
                messages.error(request, 'No se ha podido Modificar') 
            return redirect('listar_mascotas')   
        return render(request,'core/modificar_mascota.html', variables)

def servicios(request):
    return render(request, 'core/servicios.html')
