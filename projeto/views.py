from django.shortcuts import render
from .models import Projeto 

def index(request):
    dados_usuario = {"nome": "Jean Ficara com Minecraft", "idade": 24}
    return render(request, "index.html", dados_usuario) 


