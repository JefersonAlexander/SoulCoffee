from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import image_names
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=70)
    contenido=models.CharField(max_length=600)
    imagen=models.ImageField(upload_to='servicio')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo
