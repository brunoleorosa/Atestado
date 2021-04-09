from django.db import models
from datetime import datetime

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=18)

class Atestados(models.Model):
    numero_documento = models.CharField(max_length=30)
    tipo_de_servico = models.CharField(max_length=100)
    # its = models.CharField(max_length=100)
    data_emissao = models.DateField(default=datetime.now)
    empresa = models.ForeignKey(Empresa, on_delete=models.RESTRICT, null=False)
