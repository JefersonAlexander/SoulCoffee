from django.db import models
from django.contrib.auth.models import User
from tkinter import image_names
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=70)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    #def __str__(self):
        #return self.titulo

class Post(models.Model):
    titulo=models.CharField(max_length=70)
    contenido=models.CharField(max_length=1000)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    uator=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo
