from rest_framework import serializers
from .models import *

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = '__all__'

class FinaciadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiadores
        fields = '__all__'

class ColaboradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaboradores
        fields = '__all__'

class AreasTecnologicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasTecnologicas
        fields = '__all__'

