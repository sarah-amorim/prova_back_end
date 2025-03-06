from django.contrib import admin
from .models import Financiadores, AreasTecnologicas, Colaboradores, Projetos  # Registro dos modelos no admin
from .forms import FinanciadoresForm, AreasTecnologicasForm, ColaboradoresForm, ProjetosForm


class FinanciadoresAdmin(admin.ModelAdmin):
    """
    Interface administrativa para o modelo Financiadores, utilizando
    um formulário customizado para validação e entrada de dados.
    """
    form = FinanciadoresForm


class AreasTecnologicasAdmin(admin.ModelAdmin):
    """
    Interface administrativa para o modelo Áreas Tecnológicas, utilizando
    um formulário customizado para gerenciamento eficaz no admin.
    """
    form = AreasTecnologicasForm


class ColaboradoresAdmin(admin.ModelAdmin):
    """
    Interface administrativa para o modelo Colaboradores, com
    formulário customizado para facilitar a entrada de dados.
    """
    form = ColaboradoresForm


class ProjetosAdmin(admin.ModelAdmin):
    """
    Interface administrativa para o modelo Projetos. Inclui funcionalidade adicional
    para gerenciar os membros da equipe e utiliza o filtro horizontal
    para o campo de relação 'equipe'.
    """
    form = ProjetosForm
    filter_horizontal = ('equipe',)

    def save_model(self, request, obj, form, change):
        """
        Sobrescreve o método save_model para atualizar automaticamente o campo
        qtd_membros (quantidade de membros da equipe) quando o campo 'equipe'
        for alterado.
        """
        obj.save()

        # Atualiza a quantidade de membros na equipe
        if obj.equipe:
            obj.qtd_membros = obj.equipe.count()


admin.site.register(Financiadores, FinanciadoresAdmin)
admin.site.register(AreasTecnologicas, AreasTecnologicasAdmin)
admin.site.register(Colaboradores, ColaboradoresAdmin)
admin.site.register(Projetos, ProjetosAdmin)

