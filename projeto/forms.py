from django import forms
from .models import Disciplina, Modulo, Topico

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome']

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nome']

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['nome', 'conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 5}),
        }