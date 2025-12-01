from rest_framework import permissions

class EAdminOuApenasLeitura(permissions.BasePermission):
   

    def has_permission(self, request, view):
        # 1 (apenas leitura: GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            # Deixa passar apenas se o usuário estiver logado
            return request.user and request.user.is_authenticated
        
        # Só deixa passar se for da equipe (is_staff/admin)
        return request.user and request.user.is_staff

