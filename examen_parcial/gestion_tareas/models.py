from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    codigo_usuario = models.CharField(max_length=128,default='')
    password_usuario = models.CharField(max_length=128,default='')

class tarea(models.Model):
    descripcion = models.CharField(max_length=128,default='')
    fecha_creacion = models.DateField(null=True)
    fecha_entrega = models.DateField(null=True)
    responsable = models.CharField(max_length=128,default='')#nombre de usuario responsable
    estado = models.CharField(max_length=40,default='')