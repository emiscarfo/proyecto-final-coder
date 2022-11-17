from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    telefono=models.IntegerField()
    
class tecnico(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    telefono=models.IntegerField()

class tipo_servicio(models.Model):
    rubro= models.CharField(max_length=25)
    equipo=models.CharField(max_length=25)
    falla=models.CharField(max_length=25)
    detalle=models.CharField(max_length=50)
    
class presupuesto(models.Model):
    valor= models.IntegerField()
    repuestos=models.CharField(max_length=50)
    fecha_propuesta=models.DateField()
    Entregado=models.BooleanField()
    
    
    
