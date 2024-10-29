from django.shortcuts import render
from django.views.generic.list import ListView
from projMatricular.models import Alunos

# Create your views here.
def lista_alunos(request):
    # Primeiro, buscamos os funcionarios
    alunos = Alunos.objetos.all()
    # Incluímos no contexto
    contexto = {'funcionarios': alunos}
    # Retornamos o template para listar os funcionários
    return render(request, "templates/funcionarios.html", contexto)

def cria_aluno(request, pk):
    # Verificamos se o método POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_alunos'))
    # Qualquer outro método: GET, OPTION, DELETE, etc...
    else:
        return render(request, "templates/form.html", {'form': form})

class AlunoListView(ListView):
    template_name = "website/lista.html"
    model = Alunos
    context_object_name = "alunos"