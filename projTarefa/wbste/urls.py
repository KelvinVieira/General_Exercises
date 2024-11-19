from django.urls import path
from wbste import views
from wbste.views import *

app_name = 'wbste'

urlpatterns = [
    # GET /
    path('', views.index, name='index'),

    # -------------------------------------
    # GET /usuarios
    path('usuarios/', views.HomeViewUsuario.as_view(), name="usuarios_index"),

    # Path de consulta (lista) de dados
    path('usuarios/lista', ListViewUsuario.as_view(), name='usuarios_listagem'),

    # Path de alteração de dados
    path('usuarios/<pk>', UpdateViewUsuario.as_view(), name='usuarios_alteracao'),  # ou, com o uso de <slug> ao invés de <id> (<slug> trataria os dados diferentemente, em comparação a <id>)

    # Path para deleção de dados
    path('usuarios/excluir/<pk>', DeleteViewUsuario.as_view(), name='usuarios_delecao'),

    # Path para criação de dados
    path('usuarios/cadastrar/', CreateViewUsuario.as_view(), name='usuarios_criacao'),

    # ------------------------------------
    path('tarefas/', views.HomeViewTarefa.as_view(), name="tarefas_index"),

    path('tarefas/lista', ListViewTarefa.as_view(), name='tarefas_listagem'),

    path('tarefas/<pk>', UpdateViewTarefa.as_view(), name='tarefas_alteracao'),

    path('tarefas/excluir/<pk>', DeleteViewTarefa.as_view(), name='tarefas_delecao'),

    path('tarefas/cadastrar/', CreateViewTarefa.as_view(), name='tarefas_criacao'),
]
