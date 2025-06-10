from django.db import models

# Create your models here.
class Vehiculo (models.Model):
    placa= models.TextField("Placa")
    usuario_id= models.IntegerField("usuario")
    fecha_hora= models.IntegerField("fecha")

    def __str__(self):
        return f'{self.placa}'
    
    def __str__(self):
        return f'{self.fecha_hora}'