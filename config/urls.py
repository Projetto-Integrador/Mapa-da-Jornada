from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('projeto.urls')),
    path('admin/', admin.site.urls),
    path('login/', include('django.contrib.auth.urls')),  # Inclusão das URLs de autenticação do Django

]
