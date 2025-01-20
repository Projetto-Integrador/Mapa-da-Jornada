from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registre/', views.registre, name='registre'),
    path('fundamento/', views.fundamento, name='fundamento'),
    path('meuscursos/', views.meuscursos, name='meuscursos')
    path('criar_curso/', views.criar_curso, name='criar_curso'),
    path('editar_curso/<int:pk>/', views.editar_curso, name='editar_curso'),
    path('excluir_curso/<int:pk>/', views.excluir_curso, name='excluir_curso'),

]
