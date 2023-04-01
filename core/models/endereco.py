from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    numero = models.IntegerField
    complemento = models.CharField(max_length=30)

    def __str__(self):
        return self.logradouro