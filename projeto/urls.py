from django.urls import path
from . import views

app_name = 'projeto'  # Namespace do app

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registre/', views.registre, name='registre'),
    path('fundamento/', views.fundamento, name='fundamento'),
    path('meuscursos/', views.meuscursos, name='meuscursos'),
    path('paginadisciplina/', views.paginadisciplina, name='paginadisciplina'),
        
    # path('listardisciplinas', views.lista_disciplinas, name='lista_disciplinas'),
    # path('criar/', views.criar_disciplina, name='criar_disciplina'),
    # path('editar/<int:pk>/', views.editar_disciplina, name='editar_disciplina'),
    # path('excluir/<int:pk>/', views.excluir_disciplina, name='excluir_disciplina'),
    
    path('disciplinas/', views.lista_disciplinas, name='lista_disciplinas'),  # Listar disciplinas
    path('disciplinas/criar/', views.criar_disciplina, name='criar_disciplina'),  # Criar disciplina
    path('disciplinas/editar/<int:pk>/', views.editar_disciplina, name='editar_disciplina'),  # Editar disciplina
    path('disciplinas/excluir/<int:pk>/', views.excluir_disciplina, name='excluir_disciplina'),  # Excluir disciplina

]
