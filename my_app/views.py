from django.db.migrations import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjetosSerializer, ColaboradoresSerializer
from .models import *

@api_view(['GET'])
def form_projetos(request):
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
    projetos = Projetos.objects.all()
    serializer = ProjetosSerializer(projetos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def cadastrar_projeto(request):
    serializer = ProjetosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def editar_projeto(request, pk):
    projeto = Projetos.objects.get(pk=pk)
    serializer = ProjetosSerializer(instance=projeto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def inativar_projeto(request, pk):
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
    projeto = Projetos.objects.get(pk=pk)
    serializer = ProjetosSerializer(projeto)
    return Response(serializer.data)

@api_view(['GET'])
def equipe_projeto(request, pk):
    equipes = Colaboradores.objects.filter(projeto=pk)
    serializer = ColaboradoresSerializer(equipes, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def atualizar_equipe(request, pk):
    equipes = Colaboradores.objects.filter(projeto=pk)
    serializer = ColaboradoresSerializer(equipes, data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def atualizar_equipe(request, pk):
    equipes = Colaboradores.objects.get(pk=pk)
    serializer = ColaboradoresSerializer(equipes, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def listar_colaboradores(request):
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




