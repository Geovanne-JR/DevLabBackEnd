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
    serializer_class = ProjetoSerializer

    permission_classes = [EAdminOuApenasLeitura]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Projeto.objects.all() # Visitante vê tudo (o grosso)
        
        eh_professor = user.groups.filter(name='Professores').exists()
        if user.is_staff or user.is_superuser or eh_professor:
            return Projeto.objects.all()
            
        return Projeto.objects.filter(participantes=user)

    @action(detail=True, methods=['post'])
    def participantes(self, request, pk=None):
        projeto = self.get_object()
        user = request.user

        # Verifica se é Professor
        eh_professor = user.groups.filter(name='Professores').exists()

        if not (user.is_staff or eh_professor):
            return Response(
                {'erro': 'Apenas Professores ou Admins podem adicionar membros.'}, 
                status=status.HTTP_403_FORBIDDEN
            )

        usuario_id = request.data.get('usuario_id')
        usuario_alvo = get_object_or_404(Usuario, id=usuario_id)
        projeto.participantes.add(usuario_alvo)
        
        return Response({'status': f'Usuário {usuario_alvo.username} adicionado!'}, status=status.HTTP_200_OK)


    @action(detail=True, methods=['get'])
    def dashboard(self, request, pk=None):
        projeto = self.get_object()
        equipes = Equipe.objects.filter(projeto=projeto)
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
        
from django.shortcuts import render

def pagina_inicial(request):
    #  Busca todos os projetos no banco
    lista_projetos = Projeto.objects.all()
    
    # HTML desenha
    return render(request, 'index.html', {'projetos': lista_projetos})

def detalhe_projeto_view(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    
    # Verifica se é professor 
    eh_professor = False
    if request.user.is_authenticated:
        eh_professor = request.user.groups.filter(name='Professores').exists()

    return render(request, 'projeto_detalhe.html', {
        'projeto': projeto,
        'eh_professor': eh_professor
    })

from django.shortcuts import redirect
def adicionar_membro_html(request, pk):
    if request.method == 'POST':
        projeto = get_object_or_404(Projeto, pk=pk)
        # Verifica de novo se pode
        eh_prof = request.user.groups.filter(name='Professores').exists()
        
        if request.user.is_staff or eh_prof:
            uid = request.POST.get('usuario_id')
            user_add = get_object_or_404(Usuario, id=uid)
            projeto.participantes.add(user_add)
    
    return redirect('detalhe_projeto', pk=pk)
    
        