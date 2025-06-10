from django.db import models

# Create your models here.
class Usuario  (models.Model):
    nombre= models.TextField("nombre")
    apellido= models.TextField("apellido")
    correo= models.TextField("correo")
    rol_id= models.IntegerField("rol")

    def __str__(self):
        return f'{self.nombre}'
    
    def __str__(self):
        return f'{self.apellido}'
    
    def __str__(self):
        return f'{self.correo}'