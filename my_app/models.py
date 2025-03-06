from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Financiadores(models.Model):
    id_financiador = models.BigAutoField(primary_key=True)
    financiador = models.CharField(max_length=100, verbose_name="Financiador")

    def __str__(self):
        return self.financiador

class AreasTecnologicas(models.Model):
    id_area_tecnologica = models.BigAutoField(primary_key=True)
    area_tecnologica = models.CharField(max_length=100, verbose_name="Área tecnológica")

    def __str__(self):
        return self.area_tecnologica

class Colaboradores(models.Model):
    id_colaborador = models.BigAutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    nome = models.CharField(max_length=256)
    dt_nascimento = models.DateField(verbose_name="Data de nascimento")

    def __str__(self):
        return self.nome

class Projetos(models.Model):
    id_projeto = models.BigAutoField(primary_key=True)
    projeto = models.CharField(max_length=100, verbose_name="Projeto")
    financiador = models.ForeignKey(Financiadores, on_delete=models.CASCADE, verbose_name="Financiador")
    area_tecnologica = models.ForeignKey(AreasTecnologicas, on_delete=models.CASCADE, verbose_name="Área tecnológica")
    coordenador = models.CharField(max_length=100, verbose_name="Coordenador")
    ativo = models.CharField(max_length=1, choices=[('S', 'Sim'), ('N', 'Não')], default='S', verbose_name="Ativo")
    inicio_vigencia = models.DateField(verbose_name="Início de vigência")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    qtd_membros = models.IntegerField(default=0, verbose_name="Quantidade de membros")
    equipe = models.ManyToManyField(Colaboradores, related_name="projetos", verbose_name="Equipe")

    def __str__(self):
        return self.projeto


@receiver(m2m_changed, sender=Projetos.equipe.through)
def atualizar_qtd_membros(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove"]:
        instance.qtd_membros = instance.equipe.count()
        instance.save()





