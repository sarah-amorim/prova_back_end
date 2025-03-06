from django import forms
from .models import *

class FinanciadoresForm(forms.ModelForm):
    class Meta:
        model = Financiadores
        fields = '__all__'

class AreasTecnologicasForm(forms.ModelForm):
    class Meta:
        model = AreasTecnologicas
        fields = '__all__'

class ColaboradoresForm(forms.ModelForm):
    class Meta:
        model = Colaboradores
        fields = '__all__'

class ProjetosForm(forms.ModelForm):
    class Meta:
        model = Projetos
        exclude = ('qtd_membros',)
