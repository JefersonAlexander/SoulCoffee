from distutils.command.upload import upload
from http.client import PRECONDITION_FAILED
from mailbox import NoSuchMailboxError
from tkinter import CASCADE, image_names
from turtle import update
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=50, null=True)
    precio=models.CharField(max_length=50, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

        def __str__(self):
            return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)  #Tiene la clave faranea para relacionarce con la clase categoriaProd
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.IntegerField(default=0, null=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"

        

