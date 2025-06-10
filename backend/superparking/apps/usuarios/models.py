from django.db import models

# Create your models here.
class Usuario  (models.Model):
    nombre= models.TextField("nombre")
    apellido= models.TextField("apellido")
    correo= models.TextField("correo")
    rol_id= models.IntegerField("rol")