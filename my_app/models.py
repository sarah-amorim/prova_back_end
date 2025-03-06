from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Financiadores(models.Model):
    """
    Model que representa os financiadores de projetos.

    Atributos:
        id_financiador (BigAutoField): Identificador único para o financiador.
        financiador (CharField): Nome do financiador.
    """
    id_financiador = models.BigAutoField(primary_key=True)
    financiador = models.CharField(max_length=100, verbose_name="Financiador")

    def __str__(self):
        """
        Retorna uma representação textual do financiador.
        """
        return self.financiador


class AreasTecnologicas(models.Model):
    """
    Model que representa áreas tecnológicas associadas aos projetos.

    Atributos:
        id_area_tecnologica (BigAutoField): Identificador único para a área tecnológica.
        area_tecnologica (CharField): Nome da área tecnológica.
    """
    id_area_tecnologica = models.BigAutoField(primary_key=True)
    area_tecnologica = models.CharField(max_length=100, verbose_name="Área tecnológica")

    def __str__(self):
        """
        Retorna uma representação textual da área tecnológica.
        """
        return self.area_tecnologica


class Colaboradores(models.Model):
    """
    Model que representa os colaboradores que podem participar de projetos.

    Atributos:
        id_colaborador (BigAutoField): Identificador único do colaborador.
        cpf (CharField): CPF único do colaborador.
        nome (CharField): Nome completo do colaborador.
        dt_nascimento (DateField): Data de nascimento do colaborador.
    """
    id_colaborador = models.BigAutoField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    nome = models.CharField(max_length=256)
    dt_nascimento = models.DateField(verbose_name="Data de nascimento")

    def __str__(self):
        """
        Retorna o nome completo do colaborador como representação textual.
        """
        return self.nome


class Projetos(models.Model):
    """
    Model que representa os projetos vinculados a financiadores e áreas tecnológicas.

    Atributos:
        id_projeto (BigAutoField): Identificador único para o projeto.
        projeto (CharField): Nome do projeto.
        financiador (ForeignKey): Referência ao financiador do projeto.
        area_tecnologica (ForeignKey): Referência à área tecnológica do projeto.
        coordenador (CharField): Nome do coordenador do projeto.
        ativo (CharField): Indicador se o projeto está ativo (S para Sim, N para Não).
        inicio_vigencia (DateField): Data de início de vigência do projeto.
        valor (DecimalField): Valor total do projeto.
        qtd_membros (IntegerField): Quantidade atual de membros na equipe do projeto.
        equipe (ManyToManyField): Relação com os colaboradores que compõem a equipe do projeto.
    """
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
        """
        Retorna o nome do projeto como representação textual.
        """
        return self.projeto


@receiver(m2m_changed, sender=Projetos.equipe.through)
def atualizar_qtd_membros(sender, instance, action, **kwargs):
    """
    Atualiza a quantidade de membros no projeto sempre que há alterações
    na equipe (adição ou remoção de colaboradores).

    Args:
        sender (Model): O modelo que enviou o sinal.
        instance (Projetos): A instância do projeto que sofreu a mudança.
        action (str): Ação que ocorreu (post_add ou post_remove).
        **kwargs: Argumentos adicionais.
    """
    if action in ["post_add", "post_remove"]:
        instance.qtd_membros = instance.equipe.count()
        instance.save()
