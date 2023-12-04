from django.db import models
from clientes.models import Cliente

# Create your models here.
class Veiculo(models.Model):
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=100)
    descricao = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa