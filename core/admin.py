from django.contrib import admin

# Register your models here.
from .models.pessoa import Pessoa
admin.site.register(Pessoa)