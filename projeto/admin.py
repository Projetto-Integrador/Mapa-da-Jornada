from django.contrib import admin
from .models import Curso, Disciplina, Modulo, Topico

admin.site.register(Curso)

if not admin.site.is_registered(Modulo):
    @admin.register(Modulo)
    class ModuloAdmin(admin.ModelAdmin):
        list_display = ('nome', 'disciplina')  # Exibir o nome, disciplina associada e ordem do módulo
        search_fields = ('nome', 'disciplina__nome')   # Permitir buscar por nome do módulo e nome da disciplina associada
        list_filter = ('disciplina',)                   # Filtrar módulos pela disciplina associada

# Verifica se o modelo Topico já está registrado
if not admin.site.is_registered(Topico):
    @admin.register(Topico)
    class TopicoAdmin(admin.ModelAdmin):
        list_display = ('nome', 'modulo',)  # Exibir o nome e módulo associado ao tópico
        search_fields = ('nome', 'modulo__nome')  # Permitir buscar por nome do tópico e nome do módulo associado
        list_filter = ('modulo',)  # Filtrar tópicos pelo módulo associado

# Disciplina já registrada previamente
@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso')
    search_fields = ('nome', 'curso__nome')
    list_filter = ('curso',)
