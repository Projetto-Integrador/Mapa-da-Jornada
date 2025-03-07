from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

# urlpatterns = [
#     path("cadastro/", views.cadastro, name="cadastro"),
#     path("perfil/", views.perfil, name="perfil"),
#     path("editar-perfil/", views.editar_perfil, name="editar-perfil"),
#     # Customizando a view de login
#     # Redireciona pra LOGIN_REDIRECT se o usuário logado
#     # tentar acessar a página de Login
#     # O urlpatterns testa na sequência, então ele vai
#     # achar o 'login/' customizado primeiro ali em cima
#     # e desconsiderar o padrão que está abaixo.

#     # contas/urls.py

#     path('cadastro/', views.cadastro, name='cadastro'),
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
#     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
#     path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
#     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
#     path('perfil/', views.profile, name='profile'),  # Confirme que está como 'perfil/'
# ]


# contas/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("perfil/", views.perfil, name="perfil"),
    path("editar-perfil/", views.editar_perfil, name="editar-perfil"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('perfil/', views.profile, name='profile'),
]