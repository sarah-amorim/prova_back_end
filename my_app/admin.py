from django.contrib import admin
from .models import Financiadores, AreasTecnologicas, Colaboradores, Projetos  # Importe os modelos
from .forms import FinanciadoresForm, AreasTecnologicasForm, ColaboradoresForm, ProjetosForm


class FinanciadoresAdmin(admin.ModelAdmin):
    form = FinanciadoresForm

class AreasTecnologicasAdmin(admin.ModelAdmin):
    form = AreasTecnologicasForm

class ColaboradoresAdmin(admin.ModelAdmin):
    form = ColaboradoresForm

class ProjetosAdmin(admin.ModelAdmin):
    form = ProjetosForm
    filter_horizontal = ('equipe',)

    def save_model(self, request, obj, form, change):
        obj.save()

        if obj.equipe:
            obj.qtd_membros = obj.equipe.count()

admin.site.register(Financiadores, FinanciadoresAdmin)
admin.site.register(AreasTecnologicas, AreasTecnologicasAdmin)
admin.site.register(Colaboradores, ColaboradoresAdmin)
admin.site.register(Projetos, ProjetosAdmin)
