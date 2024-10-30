from django import forms

class InsereUsuarioForm(forms.Form):
    nome = forms.CharField(required=True, max_length=255)

    usernam = forms.CharField(required=True, max_length=255)

    senha = forms.CharField(required=True, max_length=14)

# class InsereFuncionarioForm(forms.ModelForm)  # Com definição de mais fields, e uso de Meta, para um ambiente mais eficiente
    # chefe = forms.BooleanField(
    # label='Este Funcionário exerce função de Chefia?',
    # required=True,
    # )
    # biografia = forms.CharField(
    # label='Biografia',
    # required=False,
    # widget=forms.TextArea
    # )
    # class Meta:
         # Modelo base
        # model = Funcionario
         # Campos que estarão no form
        # fields = [
        # 'nome',
        # 'sobrenome',
        # 'cpf',
        # 'remuneracao'
        # ]
         # Campos que não estarão no form
        # exclude = [
        # 'tempo_de_servico'
        # ]