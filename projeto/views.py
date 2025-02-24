from django.shortcuts import render, get_object_or_404, redirect
from django.forms import inlineformset_factory, modelformset_factory
from .models import Disciplina, Curso, Modulo, Topico
from .forms import DisciplinaForm, ModuloForm, TopicoForm, ModuloFormSet, TopicoFormSet

# from django.http import JsonResponse
# from .forms import CursoForm
# from django.contrib import messages


def index(request):    
    return render(request, "index.html") 

def login(request):
    return render(request, 'login.html')

def registre(request):
    return render(request, 'registre.html')

def fundamento(request):
    return render(request, 'fundamento.html')

# Disciplinas

def paginadisciplina(request, id_disciplina=None):
    if id_disciplina:
        disciplina = get_object_or_404(Disciplina, id=id_disciplina)
        return render(request, 'disciplinas/detalhe.html', {'disciplina': disciplina})
    else:
        return render(request, 'disciplinas/geral.html')  # Página padrão sem ID


def minhasdisciplinas(request):    
    return render(request, 'minhasdisciplinas.html')

def lista_disciplinas(request):
    disciplinas = Disciplina.objects.filter(curso__nome="Informática para Internet")
    return render(request, 'disciplinas/lista.html', {'disciplinas': disciplinas})



def criar_disciplina(request):
    disciplina_form = DisciplinaForm(request.POST or None)
    
    # Criando formset para módulos
    ModuloFormSet = modelformset_factory(Modulo, form=ModuloForm, extra=1)
    modulo_formset = ModuloFormSet(request.POST or None, queryset=Modulo.objects.none())
    
    # Criar dicionário de formsets de tópicos por módulo
    topico_formsets = {}
    for modulo_form in modulo_formset:
        modulo = modulo_form.instance
        if modulo and modulo.pk:  # Verifica se o módulo já existe
            topico_formsets[modulo.pk] = TopicoFormSet(
                queryset=Topico.objects.filter(modulo=modulo)
            )


    if request.method == "POST" and disciplina_form.is_valid() and modulo_formset.is_valid():
        # Salvar disciplina
        disciplina = disciplina_form.save()

        # Salvar os módulos e tópicos
        # Salvar os módulos e tópicos
        for modulo_form in modulo_formset:
            modulo = modulo_form.save(commit=False)
            modulo.disciplina = disciplina  # Relacionando com a disciplina
            modulo.save()

            # Salvar os tópicos relacionados ao módulo
            topico_formset = topico_formsets.get(modulo.pk)
            if topico_formset and topico_formset.is_valid():
                for topico_form in topico_formset:
                    topico_form.instance.modulo = modulo
                    topico_form.save()

        return redirect('projeto:lista_disciplinas')  # Redirecionar para a página de sucesso ou outra

    return render(request, 'disciplinas/form.html', {
        'disciplina_form': disciplina_form,
        'modulo_formset': modulo_formset,
        'topico_formsets': topico_formsets,
    })

def editar_disciplina(request, id_disciplina):
    # Recuperar a disciplina que estamos editando
    disciplina = get_object_or_404(Disciplina, id=id_disciplina)
    
    # Carregar o formulário da disciplina
    disciplina_form = DisciplinaForm(request.POST or None, instance=disciplina)

    # Formset para editar módulos
    ModuloFormSet = modelformset_factory(Modulo, form=ModuloForm, extra=0)
    modulo_formset = ModuloFormSet(request.POST or None, queryset=Modulo.objects.filter(disciplina=disciplina))

    # Criar formsets para tópicos
    topico_formsets = {}
    for modulo_form in modulo_formset:
        if modulo_form.instance.pk:  # Verifica se o módulo existe
            topico_formsets[modulo_form.instance.pk] = TopicoFormSet(
                request.POST or None,  # Adicionamos o POST aqui para garantir que os dados dos tópicos sejam passados corretamente
                queryset=Topico.objects.filter(modulo=modulo_form.instance)
            )

    if request.method == "POST":
        if disciplina_form.is_valid() and modulo_formset.is_valid():
            # Salvar a disciplina
            disciplina_form.save()

            # Salvar módulos
            for modulo_form in modulo_formset:
                modulo = modulo_form.save(commit=False)
                modulo.disciplina = disciplina
                modulo.save()

                # Salvar tópicos
                topico_formset = topico_formsets.get(modulo.pk)
                if topico_formset and topico_formset.is_valid():  # Verifica se o formset de tópicos é válido
                    for topico_form in topico_formset:
                        topico_form.instance.modulo = modulo
                        topico_form.save()

            return redirect('projeto:lista_disciplinas')  # Ou para outra página que você deseje

    return render(request, 'disciplinas/form.html', {
        'disciplina_form': disciplina_form,
        'modulo_formset': modulo_formset,
        'topico_formsets': topico_formsets,
        'disciplina': disciplina,
    })





def excluir_disciplina(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    disciplina.delete()
    return redirect('projeto:lista_disciplinas')  # Redireciona para a lista de disciplinas após a exclusão

def detalhe_disciplina(request, id_disciplina):
    # Recupera a disciplina específica
    disciplina = get_object_or_404(Disciplina, id=id_disciplina)
    
    # Aqui você pode passar dados adicionais, como módulos e tópicos, se necessário
    return render(request, 'disciplinas/detalhe.html', {
        'disciplina': disciplina,
    })


# Modulos
def criar_modulo(request, id_disciplina):
    disciplina = get_object_or_404(Disciplina, id=id_disciplina)
    if request.method == 'POST':
        form = ModuloForm(request.POST)
        if form.is_valid():
            modulo = form.save(commit=False)
            modulo.disciplina = disciplina
            modulo.save()
            return redirect('detalhe_disciplina', id_disciplina=disciplina.id)
    else:
        form = ModuloForm()
    return render(request, 'modulos/form.html', {'form': form, 'disciplina': disciplina})

def editar_modulo(request, id_modulo):
    modulo = get_object_or_404(Modulo, id=id_modulo)
    disciplina = modulo.disciplina
    if request.method == 'POST':
        form = ModuloForm(request.POST, instance=modulo)
        if form.is_valid():
            form.save()
            return redirect('detalhe_disciplina', id_disciplina=disciplina.id)
    else:
        form = ModuloForm(instance=modulo)
    return render(request, 'modulos/form.html', {'form': form, 'disciplina': disciplina})

def excluir_modulo(request, id_modulo):
    modulo = get_object_or_404(Modulo, id=id_modulo)
    disciplina = modulo.disciplina
    modulo.delete()
    return redirect('detalhe_disciplina', id_disciplina=disciplina.id)

# Topicos

def topico_detalhe(request, id_topico):
    topico = get_object_or_404(Topico, id=id_topico)
    return render(request, 'disciplinas/topico_detalhe.html', {'topico': topico})

def criar_topico(request, id_modulo):
    modulo = get_object_or_404(Modulo, id=id_modulo)
    if request.method == 'POST':
        form = TopicoForm(request.POST)
        if form.is_valid():
            topico = form.save(commit=False)
            topico.modulo = modulo
            topico.save()
            return redirect('detalhe_modulo', id_modulo=modulo.id)
    else:
        form = TopicoForm()
    return render(request, 'topicos/form.html', {'form': form, 'modulo': modulo})

def editar_topico(request, id_topico):
    topico = get_object_or_404(Topico, id=id_topico)
    modulo = topico.modulo
    if request.method == 'POST':
        form = TopicoForm(request.POST, instance=topico)
        if form.is_valid():
            form.save()
            return redirect('detalhe_modulo', id_modulo=modulo.id)
    else:
        form = TopicoForm(instance=topico)
    return render(request, 'topicos/form.html', {'form': form, 'modulo': modulo})

def excluir_topico(request, id_topico):
    topico = get_object_or_404(Topico, id=id_topico)
    modulo = topico.modulo
    topico.delete()
    return redirect('detalhe_modulo', id_modulo=modulo.id)


# def criar_curso(request):
#     if request.method == 'POST':
#         form = CursoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Curso cadastrado com sucesso!')
#             return redirect('index')
#         else:
#             print("Erros no formulário:", form.errors)  
#             messages.error(request, 'Erro ao cadastrar Curso!')
#     else:
#         form = CursoForm()

#     return render(request, 'criar_curso.html', {'form': form})


# def listar_curso(request):
#     cursos = CursoForm.objects.all()
#     return JsonResponse(list(cursos.values()), safe=False)


# def editar_curso(request, pk):
#     curso = get_object_or_404(CursoForm, pk=pk)
#     if request.method == 'POST':
#         form = CursoForm(request.POST, instance=curso)
#         if form.is_valid():
#             curso = form.save()
#             return JsonResponse({'id': curso.id, 'nome': curso.nome, 'descricao': curso.descricao})
#     return JsonResponse({'error': 'Erro ao editar curso'}, status=400)

# def excluir_curso(request, pk):
#     curso = get_object_or_404(CursoForm, pk=pk)
#     curso.delete()
#     return JsonResponse({'id': pk})
