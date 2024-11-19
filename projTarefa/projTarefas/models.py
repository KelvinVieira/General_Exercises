from django.db import models

# Create your models here.

# Propagando ao Django à criação do DB
class Usuario(models.Model): # Herda da classe Model
    nome = models.CharField(max_length=255, null=False, blank=False, db_column='usu_nme')
    email = models.CharField(max_length=255, null=False, blank=False, db_column='usu_email')

    objects = models.Manager()

class Tarefa(models.Model):
    descricao = models.CharField(max_length=100, null=False, blank=False, db_column='tar_descr')
    setor = models.CharField(max_length=50, null=False, blank=False, db_column='tar_setor')
    prioridade = models.CharField(max_length=50, null=False, blank=False, db_column='tar_prioridade')
    status = models.CharField(max_length=20, null=False, blank=False, db_column='tar_status')
    data = models.CharField(max_length=10, null=False, blank=False, db_column='tar_data')

    objects = models.Manager()
