from django.contrib import admin
from .models import Curso, Disciplina

admin.site.register(Curso)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso')
    search_fields = ('nome', 'curso__nome')
    list_filter = ('curso',)