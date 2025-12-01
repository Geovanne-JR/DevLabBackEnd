from django.contrib import admin
from .models import Usuario
from .models import Projeto
from .models import Equipe

admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(Equipe)

