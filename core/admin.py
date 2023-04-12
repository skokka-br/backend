from django.contrib import admin

# Register your models here.
from .models.pessoa import Pessoa
admin.site.register(Pessoa)
from .models.endereco import Endereco
admin.site.register(Endereco)
from .models.telefone import Telefone
admin.site.register(Telefone)