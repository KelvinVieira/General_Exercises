from django import forms
from projTarefas.models import *

class FormInsereUsuario(forms.ModelForm):  # Com definição de mais fields, e uso da classe interna Meta, para um ambiente mais eficiente (uso do modelo já criado models.py)
    class Meta:  # Classe interna Meta
        # Modelo base
        model = Usuario
        # Campos que estarão no form
        fields = '__all__'
        # Campos que não estarão no form
        exclude = []

class FormInsereTarefa(forms.ModelForm):
    #usuario = forms.CharField(label='p', widget=forms.TextInput)
    usuario = forms.ModelChoiceField(queryset=Tarefa.objects.all(), label='nome')  # widget=forms.TextInput
    prioridade = forms.ModelChoiceField(queryset=Tarefa.objects.all(), label='prioridade',
                                        initial=Tarefa.objects.get(prioridade='Baixa')
                                        )
    class Meta:
        model = Tarefa
        fields = '__all__'
        exclude = ['status']
