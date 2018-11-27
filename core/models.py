from django.db import models

# Create your models here.


class tipoVivienda(models.Model):
    tipovivienda = models.CharField(max_length=50,unique=True, verbose_name="Tipo de Vivienda")

    def __str__ (self):
        return self.tipovivienda
    class Meta:
        verbose_name="Tipo de Vivienda"
        verbose_name_plural = "Tipo de Viviendas"

class Raza(models.Model):
    raza = models.CharField(max_length=50,unique=True,verbose_name="Raza")
    def __str__ (self):
        return self.raza
    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"


class Estado(models.Model):
    Nombreestado = models.CharField(max_length=50,unique=True,verbose_name="Estado")
    def __str__ (self):
        return self.Nombreestado
    



class Region(models.Model):
    Nombreregion = models.CharField(max_length=50,unique=True,verbose_name="Region")    
    def __str__ (self):
        return self.Nombreregion
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"
        
class Ciudad(models.Model):
    Nombreciudad = models.CharField(max_length=50,unique=True,verbose_name="Ciudad")
    region = models.ForeignKey(Region, on_delete = models.CASCADE)
    def __str__ (self):
        return self.Nombreciudad
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class Postulante(models.Model):
    correo = models.EmailField(max_length=50,verbose_name="Correo")
    run = models.CharField(max_length=10 ,verbose_name="Run")
    nombreCompleto = models.CharField(max_length=50, verbose_name="Nombre Completo")
    fechaNaci = models.DateField (verbose_name="Fecha de nacimiento")
    telefono = models.IntegerField (verbose_name= "Telefono")
    Nombreregion = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Region")
    Nombreciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
    tipovivienda = models.ForeignKey(tipoVivienda, on_delete=models.CASCADE, verbose_name="Tipo de Vivienda")

    def __str__(self):
        return self.correo
        #return self.run
        #return self.nombreCompleto
        #return self.fechaNaci
        #return self.telefono
        #return self.Nombreregion
        #return self.Nombreciudad
        #return self.tipovivienda

class Mascota(models.Model):
    nombre = models.CharField(max_length=50,unique=True,verbose_name="Nombre")
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE,verbose_name="Raza")
    genero = models.CharField(max_length=1,verbose_name="Género")
    fechaIngreso = models.DateField(null=False, blank=True)
    fechaNacimiento = models.DateField(null=True,verbose_name="Fecha de Nacimiento")
    Nombreestado = models.ForeignKey(Estado,on_delete=models.CASCADE,verbose_name="Estado")
    imagen = models.ImageField(upload_to="media/",null=False,verbose_name="Imagen")

    def __str__ (self):
        return self.nombre
        #return self.raza
        #return self.fechaIngreso
        #return self.fechaNacimiento
        #return self.Nombreestado
        #return self.imagen

    def fecha_ingreso_formato(self):
        return self.fechaIngreso.strftime("%Y-%m-%d")

    def fecha_nacimiento_formato(self):
        return self.fechaNacimiento.strftime("%Y-%m-%d")

