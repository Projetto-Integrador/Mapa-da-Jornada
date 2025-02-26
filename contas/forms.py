from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    class Meta:
        model = Usuario
        # os campos password e password2 (confirmação) já vem
        # no UserCreationForm
        fields = ['username', 'email'] 

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "email", "avatar", "first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class UsuarioChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = Usuario
        fields = ["username", "email", "avatar", "first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Corrigindo o formato de data. O HTML reconhece como YYYY-mm-dd