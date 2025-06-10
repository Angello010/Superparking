from django.db import models

class Tiempo (models.Model):
    hora_entrada= models.IntegerField("hora de entrada")
    hora_tarifa= models.IntegerField("tarifa de timepo")
    tarifa_id= models.IntegerField("tarifa")

    def __str__(self):
        return f'{self.hora_entrada}'
    
    def __str__(self):
        return f'{self.hora_tarifa}'