# Importamos a função index() definida no arquivo views.py
from . import views
from django.urls import path
from website.views import AlunoListView
app_name = 'website'
# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    path('', views.index, name='index'),
    path('funcionarios/', AlunoListView.as_view(), name='lista_funcionarios'),
]