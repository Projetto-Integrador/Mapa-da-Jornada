from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import CursoForm
from django.contrib import messages


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




def criar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso cadastrado com sucesso!')
            return redirect('index')
        else:
            print("Erros no formulário:", form.errors)  
            messages.error(request, 'Erro ao cadastrar Curso!')
    else:
        form = CursoForm()

    return render(request, 'criar_curso.html', {'form': form})


def listar_curso(request):
    cursos = CursoForm.objects.all()
    return JsonResponse(list(cursos.values()), safe=False)


def editar_curso(request, pk):
    curso = get_object_or_404(CursoForm, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save()
            return JsonResponse({'id': curso.id, 'nome': curso.nome, 'descricao': curso.descricao})
    return JsonResponse({'error': 'Erro ao editar curso'}, status=400)

def excluir_curso(request, pk):
    curso = get_object_or_404(CursoForm, pk=pk)
    curso.delete()
    return JsonResponse({'id': pk})
