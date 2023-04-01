from django.shortcuts import render, redirect
from ..models.endereco import Endereco

def enderecohome(request):
    endereco = Endereco.objects.all()
    return render(request, "endereco.html", {"endereco": endereco})