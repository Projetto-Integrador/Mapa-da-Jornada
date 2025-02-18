from django import forms
from .models import Curso, Disciplina, Aluno




class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = "__all__"

