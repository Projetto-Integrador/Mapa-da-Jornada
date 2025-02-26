from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    # Adiciona os novos campos ao formulário padrão do Admin
    fieldsets = UserAdmin.fieldsets + (("Extra", {"fields": ("avatar", "nascimento")}),)

admin.site.register(Usuario, UsuarioAdmin)

