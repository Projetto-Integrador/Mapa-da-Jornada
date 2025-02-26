from django.urls import path
from . import views

urlpatterns = [
    # Páginas estáticas
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registre/', views.registre, name='registre'),
    path('fundamento/', views.fundamento, name='fundamento'),
    path('minhasdisciplinas/', views.minhasdisciplinas, name='minhasdisciplinas'),

    # Inscrição em disciplinas
    path('inscrever/<int:disciplina_id>/', views.inscrever, name='inscrever'),
    path('cancelar_inscrever/<int:inscricao_id>/', views.cancelar_inscrever, name='cancelar_inscrever'),


    # Para visualizar detalhes de uma disciplina
    path('disciplina/<int:id_disciplina>/', views.paginadisciplina, name='paginadisciplina'),

    # Para listar e gerenciar disciplinas
    path('disciplinas/', views.lista_disciplinas, name='lista_disciplinas'),
    path('disciplina/criar/', views.criar_disciplina, name='criar_disciplina'),
    path('<int:disciplina_id>/editar/', views.editar_disciplina, name='editar_disciplina'),
    path('<int:disciplina_id>/excluir/', views.excluir_disciplina, name='excluir_disciplina'),

    # Módulo
    
    path('<int:disciplina_id>/', views.lista_modulos, name='lista_modulos'),
    path('<int:disciplina_id>/modulo/criar/', views.criar_modulo, name='criar_modulo'),
    path('<int:disciplina_id>/modulo/<int:modulo_id>/editar/', views.editar_modulo, name='editar_modulo'),
    path('<int:disciplina_id>/modulo/<int:modulo_id>/excluir/', views.excluir_modulo, name='excluir_modulo'),

    # Tópico
    path('<int:disciplina_id>/modulo/<int:modulo_id>/', views.lista_topicos, name='lista_topicos'),
    path('<int:disciplina_id>/modulo/<int:modulo_id>/topico/criar/', views.criar_topico, name='criar_topico'),
    path('<int:disciplina_id>/modulo/<int:modulo_id>/topico/<int:topico_id>/editar/', views.editar_topico, name='editar_topico'),
    path('<int:disciplina_id>/modulo/<int:modulo_id>/topico/<int:topico_id>/excluir/', views.excluir_topico, name='excluir_topico'),
    path('<int:disciplina_id>/modulo/<int:modulo_id>/topico/<int:topico_id>/', views.detalhe_topico, name='detalhe_topico'),
]