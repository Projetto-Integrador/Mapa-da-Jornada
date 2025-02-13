from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Curso 

def index(request):
    
    return render(request, "index.html", dados_usuario) 

def login(request):
    return render(request, 'login.html')

def registre(request):
    return render(request, 'registre.html')

def fundamento(request):
    return render(request, 'fundamento.html')

def meuscursos(request):
    return render(request, 'meuscursos.html')




def criar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save()
            return JsonResponse({'id': curso.id, 'nome': curso.nome, 'descricao': curso.descricao})
    return JsonResponse({'error': 'Erro ao criar curso'}, status=400)

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save()
            return JsonResponse({'id': curso.id, 'nome': curso.nome, 'descricao': curso.descricao})
    return JsonResponse({'error': 'Erro ao editar curso'}, status=400)

def excluir_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return JsonResponse({'id': pk})
