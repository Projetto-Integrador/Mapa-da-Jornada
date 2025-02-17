from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Curso, Disciplina, Material, Aluno, AlunoCurso
from .

def index(request):
    
    return render(request, "index.html") 

def login(request):
    return render(request, 'login.html')

def registre(request):
    return render(request, 'registre.html')

def fundamento(request):
    return render(request, 'fundamento.html')

def paginadisciplina(request):
    return render(request, 'paginadisciplina.html')

def meuscursos(request):
    return render(request, 'meuscursos.html')


def listar_curso(request):
    cursos = Curso.objects.all()
    return JsonResponse(list(cursos.values()), safe=False)

def criar_curso(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        return render(request, 'criar_curso.html')

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')

    curso = 
        (nome=nome, 
        descricao=descricao)
    
    curso.save()
    return redirect(criar_curso)

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
