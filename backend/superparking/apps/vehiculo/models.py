from django.db import models

# Create your models here.
class Vehiculo (models.Model):
    placa= models.TextField("Placa")
    usuario_id= models.IntegerField("usuario")
    fecha_hora= models.IntegerField("fecha")