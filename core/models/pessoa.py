from django.db import models
from curso.models import Curso

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso)
    def __str__(self):
        return self.nome