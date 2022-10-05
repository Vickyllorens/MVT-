from django.db import models

# Create your models here.
class Familiares (models.Model):
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    tipo= models.CharField(max_length=40)
    profesion= models.CharField(max_length=40)
    fecha_de_nacimiento=models.DateField(blank=True)
    
    
    
    