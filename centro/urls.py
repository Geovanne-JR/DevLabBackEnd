from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UsuarioViewSet, ProjetoViewSet, EquipeViewSet, 
    pagina_inicial, detalhe_projeto_view, adicionar_membro_html
)


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'projetos', ProjetoViewSet, basename='projeto')
router.register(r'equipes', EquipeViewSet)


urlpatterns = [

    path('', include(router.urls)),
    

    path('home/', pagina_inicial, name='home'),
    

    path('projeto/<int:pk>/', detalhe_projeto_view, name='detalhe_projeto'),
    path('projeto/<int:pk>/add/', adicionar_membro_html, name='adicionar_membro_html'),
]