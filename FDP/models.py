from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    contraseña = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre + self.apellido

class Torneo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
    resumenDeLaFecha = models.TextField(max_length=1000, help_text="Resultados de las fechas")

    def __str__(self):
        return f"Torneo {self.nombre}, Fecha {self.fecha} /n {self.resumenDeLaFecha}"

class Equipos(models.Model):
    nombre = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre + self.puntos