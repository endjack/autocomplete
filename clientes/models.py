from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Endereço(models.Model):
    rua = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.rua

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=True)
    endereco = models.ForeignKey(Endereço, on_delete=CASCADE, null=True)
    
    def __str__(self):
        return self.nome
    
    
    

    
