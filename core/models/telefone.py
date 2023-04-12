from django.db import models

class Telefone(models.Model):
    ddd = models.CharField(max_length=5)
    numero = models.CharField(max_length=20)
    padrao = models.BooleanField(default=False)

    def __str__(self):
        return self.numero