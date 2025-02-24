from django.urls import path
from . import views

app_name = 'projeto'  # Namespace do app

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registre/', views.registre, name='registre'),
    path('fundamento/', views.fundamento, name='fundamento'),
    path('minhasdisciplinas/', views.minhasdisciplinas, name='minhasdisciplinas'),
    path('paginadisciplina/', views.paginadisciplina, name='paginadisciplina_geral'),
    path('paginadisciplina/<int:id_disciplina>/', views.paginadisciplina, name='paginadisciplina'),
            
    path('disciplinas/', views.lista_disciplinas, name='lista_disciplinas'),  # Listar disciplinas
    path('disciplinas/criar/', views.criar_disciplina, name='criar_disciplina'),
    path('disciplinas/excluir/<int:id_disciplina>/', views.excluir_disciplina, name='excluir_disciplina'),
    path('disciplinas/editar/<int:id_disciplina>/', views.editar_disciplina, name='editar_disciplina'),
    path('disciplinas/detalhe/<int:id_disciplina>/', views.detalhe_disciplina, name='detalhe_disciplina'),  # Esta linha está correta,  # Excluir disciplina

    # Modulo CRUD
    path('disciplinas/<int:id_disciplina>/modulos/criar/', views.criar_modulo, name='criar_modulo'),
    path('modulos/editar/<int:id_modulo>/', views.editar_modulo, name='editar_modulo'),
    path('modulos/excluir/<int:id_modulo>/', views.excluir_modulo, name='excluir_modulo'),
    
    # Topico CRUD
    path('modulos/<int:id_modulo>/topicos/criar/', views.criar_topico, name='criar_topico'),
    path('topicos/editar/<int:id_topico>/', views.editar_topico, name='editar_topico'),
    path('topicos/excluir/<int:id_topico>/', views.excluir_topico, name='excluir_topico'),


]
