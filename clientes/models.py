from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome