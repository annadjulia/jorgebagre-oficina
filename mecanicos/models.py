from django.db import models
from equipes.models import Equipe

# Create your models here.
class Mecanico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=100)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome