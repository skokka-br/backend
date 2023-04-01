from django.contrib import admin
from django.urls import path
from .views.pessoa import home, salvar, editar, update, delete
from .views.endereco import enderecohome

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),

    path('endereco/', enderecohome, name="endereco"),
]
