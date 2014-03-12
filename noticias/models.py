from django.db import models

# Create your models here.

class noticia(models.Model):
    titulo = models.CharField(max_length=80)
    cuerpo = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
