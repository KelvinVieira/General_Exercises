from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from wbste.forms import *

# Create your views here.
def index(request): # CRUD (Create, Read, Update, Delete)
    # Primeiro, buscamos os funcionarios
    lista = Usuario.objects.all() #busca as colecoes
    #t = loader.get_template('index.html') #indica o template
    # Incluímos no contexto
    contexto = {'usuarios': lista}
    # Retornamos o template para listar os funcionários
    return render(request, "wbste/index.html", contexto)

class HomeViewUsuario(TemplateView):
    template_name = "wbste/usuario/index.html"

class ListViewUsuario(ListView):
    template_name = "wbste/usuario/lista.html"
    model = Usuario
    context_object_name = "usuarios"

class UpdateViewUsuario(UpdateView):
    template_name = 'atualiza.html'
    model = Usuario
    fields = [
        'nome',
        'email'
    ]  # ou, fields = '__all__'
    context_object_name = 'usuarios'

    def get_object(self, queryset=None):
        usuario = None

        # Os campos {pk} e {slug} estão presentes em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            # Busca o funcionario apartir do id
            usuario = Usuario.objects.filter(id=id).first()

        return usuario

class DeleteViewUsuario(DeleteView):
    template_name = "wbste/usuario/exclui.html"
    model = Usuario
    context_object_name = 'usuarios'
    success_url = reverse_lazy("wbste:usuarios_listagem")

    def get_object(self, queryset=None):
        usuario = None

        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            usuario = Usuario.objects.filter(id=id).first()

        return usuario

class CreateViewUsuario(CreateView):
    template_name = "wbste/usuario/cria.html"
    model = Usuario
    form_class = FormInsereUsuario
    success_url = reverse_lazy("wbste:usuarios_listagem")

# -------------------------------------------------
class HomeViewTarefa(TemplateView):
    template_name = "wbste/tarefa/index.html"

class ListViewTarefa(ListView):
    template_name = "wbste/tarefa/lista.html"
    model = Tarefa
    context_object_name = "tarefas"

class UpdateViewTarefa(UpdateView):
    template_name = 'atualiza.html'
    model = Tarefa
    fields = '__all__'
    context_object_name = 'tarefas'

    def get_object(self, queryset=None):
        tarefa = None

        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            tarefa = Tarefa.objects.filter(id=id).first()

        return tarefa

class DeleteViewTarefa(DeleteView):
    template_name = "wbste/tarefa/exclui.html"
    model = Tarefa
    context_object_name = 'tarefas'
    success_url = reverse_lazy("wbste:tarefas_listagem")

    def get_object(self, queryset=None):
        tarefa = None

        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            tarefa = Tarefa.objects.filter(id=id).first()

        return tarefa

class CreateViewTarefa(CreateView):
    template_name = "wbste/tarefa/cria.html"
    model = Tarefa
    form_class = FormInsereTarefa
    success_url = reverse_lazy("wbste:tarefas_listagem")
