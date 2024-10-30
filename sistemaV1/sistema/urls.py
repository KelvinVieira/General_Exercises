"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from web.views import UsuarioListView, UsuarioUpdateView, UsuarioDeleteView, UsuarioCreateView

urlpatterns = [
    # Interface administrativa (auto-gerada, junto aos outros pacotes gerados automaticamente pelo assistente django-admin)
    path('admin/', admin.site.urls),

    # Inclusão de URLs do app website
    path('', include('web.urls', namespace='web')),

    # Path de consulta (lista) de dados
    path('usuarios/', UsuarioListView.as_view(), name='lista_usuarios'),

    # Path de alteração de dados
    path('usuario/<id>', UsuarioUpdateView.as_view(), name='atualiza_usuarios'),  # ou, com o uso de <slug> ao invés de <id> (<slug> trataria os dados diferentemente, em comparação a <id>)

    # Path para deleção de dados
    path('usuario/excluir/<pk>', UsuarioDeleteView.as_view(), name='deleta_usuarios'),

    # Path para criação de dados
    path('usuario/cadastrar/', UsuarioCreateView.as_view(), name='cadastra_usuarios'),
]
