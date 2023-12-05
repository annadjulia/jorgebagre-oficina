from django.db import models
from django.db.models.fields import CharField
from veiculos.models import Veiculo
from equipes.models import Equipe

# Create your models here.
class Ordem(models.Model):
    dataEmissao = models.DateField()
    dataEntrega = models.DateField()
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    veiculo_id = models.ForeignKey('veiculos.Veiculo', on_delete=models.CASCADE)
    equipe_id = models.ForeignKey('equipes.Equipe', on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao