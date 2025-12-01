from rest_framework import viewsets
from .models import Usuario, Projeto, Equipes
from .serializers import UsuarioSerializer, ProjetoSerializer, EquipesSerializer

# 1. View do Usuário
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()          # Pega todos os usuários do banco
    serializer_class = UsuarioSerializer      # Usa o tradutor de usuários

# 2. View do Projeto
class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()          # Pega todos os projetos
    serializer_class = ProjetoSerializer      # Usa o tradutor de projetos

# 3. View da Equipe
class EquipesViewSet(viewsets.ModelViewSet):
    queryset = Equipes.objects.all()           # Pega todas as equipes
    serializer_class = EquipesSerializer       # Usa o tradutor de equipes