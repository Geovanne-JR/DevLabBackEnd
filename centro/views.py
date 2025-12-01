from rest_framework import viewsets
from .models import Usuario, Projeto, Equipe
from .serializers import UsuarioSerializer, ProjetoSerializer, EquipeSerializer

# 1. View do Usuário
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()          # Pega todos os usuários do banco
    serializer_class = UsuarioSerializer      # Usa o tradutor de usuários

# 2. View do Projeto
class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()          # Pega todos os projetos
    serializer_class = ProjetoSerializer      # Usa o tradutor de projetos

# 3. View da Equipe
class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()           # Pega todas as equipes
    serializer_class = EquipeSerializer       # Usa o tradutor de equipes