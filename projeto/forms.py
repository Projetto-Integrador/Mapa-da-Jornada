from django import forms
from .models import Curso, Disciplina

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'descricao', 'curso']  # Adicionando o campo 'curso'
