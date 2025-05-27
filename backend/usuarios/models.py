from django.db import models

# Create your models here.
class Usuario  (models.model):
    nombre= models.TextField("nombre")
    apellido= models.TextField("apellido")
    correo= models.TextField("correo")
    rol_id= models.IntegerField("rol")