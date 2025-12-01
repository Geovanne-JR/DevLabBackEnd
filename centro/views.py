from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

#  Permissões
from rest_framework.permissions import IsAuthenticated
# regras
from .permissions import EAdminOuApenasLeitura 

from .models import Usuario, Projeto, Equipe
from .serializers import UsuarioSerializer, ProjetoSerializer, EquipeSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def projetos(self, request, pk=None):
        usuario = self.get_object()
        projetos = Projeto.objects.filter(participantes=usuario)
        serializer = ProjetoSerializer(projetos, many=True)
        return Response(serializer.data)

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    permission_classes = [EAdminOuApenasLeitura]

    # Rota existente (Adicionar participantes)
    @action(detail=True, methods=['post'])
    def participantes(self, request, pk=None):
        projeto = self.get_object()
        usuario_id = request.data.get('usuario_id')
        usuario = get_object_or_404(Usuario, id=usuario_id)
        projeto.participantes.add(usuario)
        return Response({'status': f'Usuário {usuario.username} adicionado!'}, status=status.HTTP_200_OK)


    @action(detail=True, methods=['get'])
    def dashboard(self, request, pk=None):
        projeto = self.get_object()
        
        # 1. Pega todas as equipes desse projeto
        equipes = Equipe.objects.filter(projeto=projeto)
        
        # 2. Monta um JSON com tudo misturado
        dados_equipes = []
        for equipe in equipes:
            dados_equipes.append({
                "nome_equipe": equipe.nome,
                "lider": equipe.lider.username if equipe.lider else "Sem líder",
                "total_membros": equipe.membros.count(),
                "membros": [membro.username for membro in equipe.membros.all()]
            })

        dados_completo = {
            "projeto": projeto.titulo,
            "status": projeto.status,
            "cliente": projeto.cliente,
            "equipes": dados_equipes
        }
        
        return Response(dados_completo)



class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    # Admin edita, aluno só lê.
    permission_classes = [EAdminOuApenasLeitura]


    @action(detail=True, methods=['post'])
    def definir_lider(self, request, pk=None):
        equipe = self.get_object()
        usuario_id = request.data.get('usuario_id')
        usuario = get_object_or_404(Usuario, id=usuario_id)
        try:
            equipe.lider = usuario
            equipe.save()
            return Response({'status': f'Líder definido: {usuario.username}'})
        except Exception as e:
            return Response({'erro': 'Usuário já é líder ou erro interno.'}, status=status.HTTP_400_BAD_REQUEST)
        