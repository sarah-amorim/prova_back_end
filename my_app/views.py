from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjetosSerializer, ColaboradoresSerializer
from .models import *


@api_view(['GET'])
def form_projetos(request):
    """
    Retorna uma estrutura JSON base para cadastro de novos projetos.

    Este formulário contém chaves predefinidas como 'projeto', 'financiador',
    'area_tecnologica', 'coordenador', dentre outras.

    Retorno:
        Response: Um dicionário JSON com a estrutura de um projeto vazio.
    """
    form = {
        "projeto": "",
        "financiador": "",
        "area_tecnologica": "",
        "coordenador": "",
        "ativo": "S",
        "inicio_vigencia": "",
        "valor": 0.00,
        "qtd_membros": 0,
        "equipe": []
    }
    return Response(form)


@api_view(['GET'])
def listar_projetos(request):
    """
    Lista todos os projetos armazenados no banco de dados.

    Retorno:
        Response: Uma lista de projetos serializada em formato JSON.
    """
    projetos = Projetos.objects.all()
    serializer = ProjetosSerializer(projetos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def cadastrar_projeto(request):
    """
    Cadastra um novo projeto no banco de dados.

    Args:
        request (Request): Dados enviados no corpo da requisição para criar o novo projeto.

    Retorno:
        Response: Dados do projeto criado (status 201) ou erros de validação (status 400).
    """
    serializer = ProjetosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def editar_projeto(request, pk):
    """
    Atualiza os dados completos de um projeto existente.

    Args:
        request (Request): Dados JSON fornecidos para atualizar o projeto.
        pk (int): ID do projeto que será atualizado.

    Retorno:
        Response: Dados atualizados do projeto ou erros de validação.
    """
    projeto = Projetos.objects.get(pk=pk)
    serializer = ProjetosSerializer(instance=projeto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def inativar_projeto(request, pk):
    """
    Marca um projeto como inativo no sistema.

    Args:
        pk (int): O ID do projeto a ser inativado.

    Retorno:
        Response: Status HTTP 204 indicando sucesso.
    """
    projeto = Projetos.objects.get(pk=pk)
    projeto.ativo = False
    projeto.save()
    return Response(status=204)


@api_view(['PATCH'])
def editar_projeto(request, pk):
    projeto = Projetos.objects.get(pk=pk)
    serializer = ProjetosSerializer(instance=projeto, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def visualizar_projeto(request, pk):
    """
    Retorna os detalhes de um projeto específico.

    Args:
        pk (int): ID do projeto a ser visualizado.

    Retorno:
        Response: Um dicionário JSON com os detalhes do projeto solicitado.
    """
    projeto = Projetos.objects.get(pk=pk)
    serializer = ProjetosSerializer(projeto)
    return Response(serializer.data)


@api_view(['GET'])
def equipe_projeto(request, pk):
    """
    Retorna a lista de colaboradores vinculados a um projeto específico.

    Args:
        pk (int): ID do projeto cujos membros da equipe serão listados.

    Retorno:
        Response: Uma lista JSON contendo os dados dos colaboradores do projeto.
    """
    equipes = Colaboradores.objects.filter(projeto=pk)
    serializer = ColaboradoresSerializer(equipes, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
def atualizar_equipe(request, pk):
    """
    Atualiza a equipe vinculada a um projeto específico.

    Args:
        request (Request): Dados enviados no corpo da requisição.
        pk (int): ID do projeto cuja equipe será atualizada.

    Retorno:
        Response: Uma lista JSON com os dados dos colaboradores atualizados.
    """
    equipes = Colaboradores.objects.filter(projeto=pk)
    serializer = ColaboradoresSerializer(equipes, data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PATCH'])
def atualizar_equipe_colaborador(request, pk):
    """
    Atualiza os detalhes de um colaborador específico de uma equipe.

    Args:
        request (Request): Dados enviados no corpo da requisição.
        pk (int): ID do colaborador a ser atualizado.

    Retorno:
        Response: Um dicionário JSON com os dados do colaborador atualizado.
    """
    equipes = Colaboradores.objects.get(pk=pk)
    serializer = ColaboradoresSerializer(equipes, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def listar_colaboradores(request):
    """
    Lista todos os colaboradores cadastrados no banco de dados.

    Retorno:
        Response: Uma lista JSON contendo os dados de todos os colaboradores.
    """
    colaboradores = Colaboradores.objects.all()
    serializer = ColaboradoresSerializer(colaboradores, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def cadastrar_colaboradores(request):
    serializer = ColaboradoresSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def visualizar_colaboradores(request, pk):
    """
    Retorna os dados de um colaborador específico.

    Args:
        pk (int): ID do colaborador a ser visualizado.

    Retorno:
        Response: Um dicionário JSON com os dados do colaborador solicitado.
    """
    colaborador = Colaboradores.objects.get(pk=pk)
    serializer = ColaboradoresSerializer(colaborador)
    return Response(serializer.data)


@api_view(['PATCH'])
def editar_colaboradores(request, pk):
    colaborador = Colaboradores.objects.get(pk=pk)
    serializer = ColaboradoresSerializer(colaborador, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

