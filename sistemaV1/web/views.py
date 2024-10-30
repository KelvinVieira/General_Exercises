from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from sistema.models import Usuario
from web.forms import InsereUsuarioForm

# Create your views here.
def lista_usuarios(request):  # CRUD (Create, Read, Update, Delete)
    # Primeiro, buscamos os funcionarios
    usuarios = Usuario.objetos.all()
    # Incluímos no contexto
    contexto = {'usuarios': usuarios}
    # Retornamos o template para listar os funcionários
    return render(request, "templates/usuarios.html", contexto)

def cria_usuario(request, pk):
    # Verificamos se o mét odo POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_usuarios'))
    # Qualquer outro mét odo: GET, OPTION, DELETE, etc...
    else:
        return render(request, "templates/form.html", {'form': form})

class UsuarioListView(ListView):
    template_name = "web/lista.html"
    model = Usuario
    context_object_name = "usuarios"

class UsuarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Usuario
    fields = '__all__'
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        usuario = None

        # O campo {pk} é presente em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            # Busca o funcionario apartir do id
            usuario = Usuario.objetos.filter(id=id).first()

        return usuario

class UsuarioDeleteView(DeleteView):
    template_name = "web/exclui.html"
    model = Usuario
    context_object_name = 'usuario'
    success_url = reverse_lazy("web:lista_usuarios")

    def get_object(self, queryset=None):
        usuario = None

        id = self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            usuario = Usuario.objetos.filter(id=id).first()

        return usuario

class UsuarioCreateView(CreateView):
    template_name = "web/cria.html"
    model = Usuario
    form_class = InsereUsuarioForm
    success_url = reverse_lazy("web:lista_usuarios")