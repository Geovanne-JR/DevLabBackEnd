from rest_framework import serializers
from .models import Usuario, Projeto, Equipe 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'cargo'] 

class ProjetoSerializer(serializers.ModelSerializer):
    # mostrar os detalhes
    participantes_detalhes = UsuarioSerializer(source='participantes', many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = '__all__'

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'