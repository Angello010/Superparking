from django.db import models

# Create your models here.
class Tiempo (models.model):
    hora_entrada= models.IntegerField("hora de entrada")
    hora_tarifa= models.IntegerField("tarifa de timepo")
    tarifa_id= models.IntegerField("tarifa")