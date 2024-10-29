from django.db import models

# Create your models here.
class Alunos(models.Model): # Herda da classe Model
    nome = models.CharField(
        max_length=255, null=False, blank=False
    )

    sobrenome = models.CharField(
        max_length=255, null=False, blank=False
    )

    cpf = models.CharField(
        max_length=14, null=False, blank=False
    )

    celular = models.CharField(
        max_length=14, null=False, blank=False
    )

    email = models.CharField(
        max_length=14, null=False, blank=False
    )

    objetos = models.Manager()