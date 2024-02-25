from django.db import models
from django.contrib.auth.models import User


class USUARIO (User): 
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contraseña= models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    

# Create your models here.
# class Departamento(models.Model):
#     nombre = models.CharField(max_length=50)
#     direccion = models.CharField(max_length=100)
#     habitaciones=   models.IntegerField()
#     disponible= models.BooleanField()
#     precio= models.IntegerField()
#     metros_cuadrados= models.IntegerField()
#     banos= models.IntegerField()
#     garaje= models.BooleanField()
#     descripcion = models.CharField(max_length=100)
#     ubicacion = models.CharField(max_length=50)
#     def __str__(self):
#         return self.nombre
    
# class Fotos (models.Model):
#     departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
#     #imagen = models.ImageField(upload_to="fotos")
#     imagen_descripcion = models.CharField(max_length=100)
#     def __str__(self):
#         return self.imagen_descripcion

# class Favoritos(models.Model):
#     departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
#     usuario = models.CharField(max_length=50)
#     def __str__(self):
#         return self.usuario
    
# class Agentes(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     telefono = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     direccion = models.CharField(max_length=50)
#     #foto= models.ImageField(upload_to="agentes")
#     tipo= models.CharField(max_length=50)
#     def __str__(self):
#         return self.nombre
    
# class Localidades(models.Model):
#     nombre = models.CharField(max_length=50)
#     coordenadas = models.CharField(max_length=50)
#     cod_postal= models.CharField(max_length=50)
#     def __str__(self):
#         return self.nombre
    
# class Usuarios(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     telefono = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     direccion = models.CharField(max_length=50)
#     def __str__(self):
#         return self.nombre
    