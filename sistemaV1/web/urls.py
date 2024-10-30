# Importamos a função index() definida no arquivo views.py
from . import views
from django.urls import path
from web.views import UsuarioListView
app_name = 'web'
# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    #path('', views.index, name='index'),
    path('usuarios/', UsuarioListView.as_view(), name='lista_usuarios'),
]