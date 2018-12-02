from rest_framework import serializers
from apps.funcionarios.models import Funcionario


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome', 'departamentos', 'empresa', 'user', 'imagem')
