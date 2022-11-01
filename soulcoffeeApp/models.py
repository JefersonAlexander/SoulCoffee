from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import image_names
from tkinter.tix import Tree
from django.db import models

# Create your models here.

class Presentacion(models.Model):
    titulo=models.CharField(max_length=70)
    contenido=models.CharField(max_length=900)
    contenido1=models.CharField(max_length=600, null=True, blank=True)
    imagen=models.ImageField(upload_to='servicio', null=True, blank=True)
   

    class Meta:
        verbose_name='presentacion'
        verbose_name_plural='presentaciones'

    def __str__(self):
        return self.titulo

