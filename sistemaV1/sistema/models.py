from django.db import models

# Create your models here.

# Propagando ao Django à criação do DB
class Usuario(models.Model): # Herda da classe Model
    nome = models.CharField(max_length=255, null=False, blank=False)

    username = models.CharField(max_length=255, null=False, blank=False)

    senha = models.CharField(max_length=14, null=False, blank=False)

    objetos = models.Manager()