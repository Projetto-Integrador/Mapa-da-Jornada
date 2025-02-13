from django import forms
from .models import Curso

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome_aluno', 'email_aluno', 'curso'] 

    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), empty_label="Escolha um curso", widget=forms.Select)
