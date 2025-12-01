from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ProjetoViewSet, EquipeViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'projetos', ProjetoViewSet)
router.register(r'equipes', EquipeViewSet)

urlpatterns = [

    path('', include(router.urls)),
]