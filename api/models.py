from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Usuario(models.Model):
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    totalReports = models.IntegerField()
    pswd = models.CharField(max_length=50)

class Modalidad(models.Model):
    nombre = models.CharField(max_length=50)

class Reports(models.Model):
    dia= models.DateField()
    hora= models.TimeField()
    descripcion = models.CharField(max_length=150)
    titulo= models.CharField(max_length=50, null=True, blank=True)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    modalidad= models.ForeignKey(Modalidad, null=True, blank=True,on_delete=models.CASCADE)

class Cais(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

