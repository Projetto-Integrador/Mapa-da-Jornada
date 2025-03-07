# projeto/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from .models import Disciplina, Curso, Modulo, Topico, Inscricao
from .forms import DisciplinaForm, ModuloForm, TopicoForm  # Certifique-se de que estão em forms.py

def index(request):
    curso, created = Curso.objects.get_or_create(nome="Informática para Internet")
    print(f"Index - Usuário logado: {request.user if request.user.is_authenticated else 'Anônimo'}")
    disciplinas = curso.disciplinas.all()
    return render(request, 'index.html', {'disciplinas': disciplinas})

def login(request):
    return render(request, 'login.html')

def registre(request):
    return render(request, 'registre.html')

def fundamento(request):
    return render(request, 'fundamento.html')

@login_required
def minhasdisciplinas(request):
    usuario = request.user
    inscricoes = Inscricao.objects.filter(usuario=usuario).order_by('disciplina__nome')
    print(f"Minhas Disciplinas - Usuário logado: {usuario}, Inscrições: {[i.disciplina.nome for i in inscricoes]}")
    paginator = Paginator(inscricoes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'minhasdisciplinas.html', {'page_obj': page_obj})

@login_required
def inscrever(request, disciplina_id):
    if request.method == 'POST':
        disciplina = get_object_or_404(Disciplina, id=disciplina_id)
        inscricao, created = Inscricao.objects.get_or_create(usuario=request.user, disciplina=disciplina)
        print(f"Inscrição - Usuário logado: {request.user}, Disciplina: {disciplina.nome}, Criada: {created}")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if created:
                return JsonResponse({'success': True, 'message': f"Você se inscreveu em {disciplina.nome} com sucesso!"})
            return JsonResponse({'success': False, 'message': f"Você já está inscrito em {disciplina.nome}."})
        if created:
            messages.success(request, f"Você se inscreveu em {disciplina.nome} com sucesso!")
        else:
            messages.info(request, f"Você já está inscrito em {disciplina.nome}.")
        return redirect('minhasdisciplinas')
    return redirect('index')

@login_required
def cancelar_inscrever(request, inscricao_id):
    if request.method == 'POST':
        inscricao = get_object_or_404(Inscricao, id=inscricao_id, usuario=request.user)
        disciplina_nome = inscricao.disciplina.nome
        inscricao.delete()
        print(f"Cancelamento - Usuário logado: {request.user}, Disciplina: {disciplina_nome}")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': f"Inscrição em {disciplina_nome} cancelada com sucesso!"})
        messages.success(request, f"Inscrição em {disciplina_nome} cancelada com sucesso!")
    return redirect('minhasdisciplinas')

@login_required
def paginadisciplina(request, id_disciplina=None):
    if id_disciplina:
        disciplina = get_object_or_404(Disciplina, id=id_disciplina)
        print(f"Disciplina: {disciplina.nome}, Módulos: {list(disciplina.modulos.all())}")
        return render(request, 'paginadisciplina.html', {'disciplina': disciplina})
    else:
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas/geral.html', {'disciplinas': disciplinas})

@login_required
def lista_disciplinas(request):
    if not request.user.is_staff:
        messages.error(request, "Acesso negado. Apenas administradores podem ver esta página.")
        return redirect('index')
    curso = Curso.objects.get(nome="Informática para Internet")
    disciplinas = curso.disciplinas.all()
    return render(request, 'disciplinas/lista_disciplinas.html', {'disciplinas': disciplinas})

def criar_disciplina(request):
    curso = Curso.objects.get(nome="Informática para Internet")
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.curso = curso
            disciplina.save()
            return redirect('lista_disciplinas')
    else:
        form = DisciplinaForm()
    return render(request, 'disciplinas/criar_disciplina.html', {'form': form})

def editar_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('lista_disciplinas')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'disciplinas/editar_disciplina.html', {'form': form, 'disciplina': disciplina})

def excluir_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('lista_disciplinas')
    return render(request, 'disciplinas/excluir_disciplina.html', {'disciplina': disciplina})

# Módulo
def lista_modulos(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    modulos = disciplina.modulos.all()
    return render(request, 'disciplinas/lista_modulos.html', {'disciplina': disciplina, 'modulos': modulos})

def criar_modulo(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    if request.method == 'POST':
        form = ModuloForm(request.POST)
        if form.is_valid():
            modulo = form.save(commit=False)
            modulo.disciplina = disciplina
            modulo.save()
            return redirect('lista_modulos', disciplina_id=disciplina_id)
    else:
        form = ModuloForm()
    return render(request, 'disciplinas/criar_modulo.html', {'form': form, 'disciplina': disciplina})

# ... (outras views de módulo e tópico seguem sem mudanças)

def editar_modulo(request, disciplina_id, modulo_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    modulo = get_object_or_404(Modulo, id=modulo_id, disciplina=disciplina)
    if request.method == 'POST':
        form = ModuloForm(request.POST, instance=modulo)
        if form.is_valid():
            form.save()
            return redirect('lista_modulos', disciplina_id=disciplina_id)  # Corrigido
    else:
        form = ModuloForm(instance=modulo)
    return render(request, 'disciplinas/editar_modulo.html', {'form': form, 'modulo': modulo, 'disciplina': disciplina})

def excluir_modulo(request, disciplina_id, modulo_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    modulo = get_object_or_404(Modulo, id=modulo_id, disciplina=disciplina)
    if request.method == 'POST':
        modulo.delete()
        return redirect('lista_modulos', disciplina_id=disciplina_id)
    return render(request, 'disciplinas/excluir_modulo.html', {'modulo': modulo, 'disciplina': disciplina})

# --- Tópico ---
def lista_topicos(request, disciplina_id, modulo_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    modulo = get_object_or_404(Modulo, id=modulo_id, disciplina=disciplina)
    topicos = modulo.topicos.all()
    return render(request, 'disciplinas/lista_topicos.html', {'disciplina': disciplina, 'modulo': modulo, 'topicos': topicos})

def criar_topico(request, disciplina_id, modulo_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    modulo = get_object_or_404(Modulo, id=modulo_id, disciplina=disciplina)
    if request.method == 'POST':
        form = TopicoForm(request.POST)
        if form.is_valid():
            topico = form.save(commit=False)
            topico.modulo = modulo
            topico.save()
            return redirect('lista_topicos', disciplina_id=disciplina_id, modulo_id=modulo_id)  # Corrigido
    else:
        form = TopicoForm()
    return render(request, 'disciplinas/criar_topico.html', {'form': form, 'modulo': modulo, 'disciplina': disciplina})

def editar_topico(request, disciplina_id, modulo_id, topico_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    modulo = get_object_or_404(Modulo, id=modulo_id, disciplina=disciplina)
    topico = get_object_or_404(Topico, id=topico_id, modulo=modulo)
    if request.method == 'POST':
        form = TopicoForm(request.POST, instance=topico)
        if form.is_valid():
            form.save()
            return redirect('lista_topicos', disciplina_id=disciplina_id, modulo_id=modulo_id)
    else:
        form = TopicoForm(instance=topico)
    return render(request, 'disciplinas/editar_topico.html', {'form': form, 'topico': topico, 'modulo': modulo, 'disciplina': disciplina})

def excluir_topico(request, disciplina_id, modulo_id, topico_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    modulo = get_object_or_404(Modulo, id=modulo_id, disciplina=disciplina)
    topico = get_object_or_404(Topico, id=topico_id, modulo=modulo)
    if request.method == 'POST':
        topico.delete()
        return redirect('lista_topicos', disciplina_id=disciplina_id, modulo_id=modulo_id)
    return render(request, 'disciplinas/excluir_topico.html', {'topico': topico, 'modulo': modulo, 'disciplina': disciplina})

def detalhe_topico(request, disciplina_id, modulo_id, topico_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    modulo = get_object_or_404(Modulo, id=modulo_id, disciplina=disciplina)
    topico = get_object_or_404(Topico, id=topico_id, modulo=modulo)
    return render(request, 'disciplinas/detalhe_topico.html', {'disciplina': disciplina, 'modulo': modulo, 'topico': topico})