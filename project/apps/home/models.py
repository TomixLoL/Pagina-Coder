from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre