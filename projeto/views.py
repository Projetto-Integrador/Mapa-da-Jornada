from django.shortcuts import render
from .models import Projeto 

def index(request):
    dados_usuario = {"nome": "Jean Ficara com Minecraft", "idade": 24}
    return render(request, "index.html", dados_usuario) 

def login(request):
    return render(request, 'login.html')

def registre(request):
    return render(request, 'registre.html')

def fundamento(request):
    return render(request, 'fundamento.html')

def meuscursos(request):
    return render(request, 'meuscursos.html')