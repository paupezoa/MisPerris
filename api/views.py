from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
#el serializer permite transformar un arreglo en un json
from django.core import serializers
import json
from core.models import Postulante, Mascota , Region , Ciudad , tipoVivienda ,Estado, Raza

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
#importamos el modelo para guardar el token
from fcm_django.models import FCMDevice
# Create your views here.

@csrf_exempt
@require_http_methods(['POST'])
def agregar_token(request):
    body  = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    #obtenemos el token
    token = bodyDict['token']

    #primero verificamos que el token no exista en la BBDD para guardarlo
    existe = FCMDevice.objects.filter(registration_id=token, active=True)

    if existe:
        return HttpResponseBadRequest(json.dumps({'mensaje':'El token ya existe'}), content_type="application/json")
    

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    #solo si el usuario esta autenticado lo asociaremos con el token
    if request.user.is_authenticated:
        dispositivo.user = request.user
    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'El token fue almacenado'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar el token'}), content_type="application/json")



#crearemos un view que muestre el listado de automoviles
#en formato json

def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    #transformamos los datos a json
    mascotasJson = serializers.serialize('json', mascotas)

    #mostramos el json en el navegador
    return HttpResponse(mascotasJson, content_type="application/json")

#POST
@csrf_exempt
@require_http_methods(['POST'])
def agregar_mascota(request):
    #obtenemos el body del request
    body = request.body.decode('utf-8')
    #el body viene como un string, por lo que lo transformamos
    bodyDict = json.loads(body)

    #guardaremos el automovil en la BBDD
    mascota = Mascota()
    mascota.nombre = bodyDict['nombre']
    mascota.raza = Raza(id=bodyDict['raza_id'])
    mascota.genero  = bodyDict['genero']
    mascota.fechaIngreso = bodyDict['fechaIngreso']
    mascota.fechaNacimiento = bodyDict['fechaNacimiento']
    mascota.Nombreestado = Estado(id=bodyDict['Nombreestado'])
    #mascota.imagen = bodyDict['imagen']

    mascota.save()
    try:
        return HttpResponse(json.dumps({'mensaje':'Guardado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):

    try:
        #primero buscamos el automovil que eliminaremos
        mascota = Mascota.objects.get(id=id)
        mascota.delete()
        return HttpResponse(json.dumps({'mensaje':'eliminado correctamente'}),
         content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':"no se ha podido eliminar"}),
        content_type="application/json")
    

#POST
@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    #obtenemos el body del request
    body = request.body.decode('utf-8')
    #el body viene como un string, por lo que lo transformamos
    bodyDict = json.loads(body)

    #guardaremos el automovil en la BBDD
    mascota = Mascota()
    mascota.id = bodyDict['id']
    mascota.nombre = bodyDict['nombre']
    mascota.raza = Raza(id=bodyDict['raza_id'])
    mascota.genero  = bodyDict['genero']
    mascota.fechaIngreso = bodyDict['fechaIngreso']
    mascota.fechaNacimiento = bodyDict['fechaNacimiento']
    mascota.Nombreestado = Estado(id=bodyDict['Nombreestado'])
    #mascota.imagen = bodyDict['imagen']

    try:
        mascota.save()
        return HttpResponse(json.dumps({'mensaje':'Modificado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido modificar'}), content_type="application/json")

