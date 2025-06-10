from django.db import models

# Create your models here.
class Tiempodeparqueo (models.Model):
    precio= models.IntegerField("Precio")