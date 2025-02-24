from django import forms
from django.forms import inlineformset_factory 
from .models import Curso, Disciplina, Modulo, Topico

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'descricao', 'curso']  # Adicionando o campo 'curso'

# Formulário para Módulo
class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nome', 'ordem']  # Adicionando o campo 'disciplina'

# Formulário para Tópico
class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['nome', 'descricao'] # Adicionando o campo 'descricao'

# Criar um formset para Módulos
ModuloFormSet = inlineformset_factory(
    Disciplina, Modulo, form=ModuloForm, fields=['nome', 'ordem'], extra=1
)

# Criar um formset para Tópicos
TopicoFormSet = inlineformset_factory(
    Modulo, Topico, form=TopicoForm, fields=['nome', 'descricao'], extra=1
)
