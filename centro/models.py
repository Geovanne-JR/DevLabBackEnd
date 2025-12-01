from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    pass

class Projeto(models.Model):
    EscolhasStatus = [
        ('planejado', 'Planejado'),
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    ]
    titulo = models.CharField(max_length=200)
    cliente = models.CharField(max_length=100)
    descricao = models.TextField()
    data_Inicio = models.DateField()
    data_Fim_Prevista = models.DateField()
    status = models.CharField(max_length=20, choices = EscolhasStatus , default = 'planejado')
    participantes = models.ManyToManyField(Usuario, related_name='projetos_participados', blank=True)

    def __str__(self):
        return self.titulo
class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(blank= True, null=  True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE , related_name= 'equipes')

    lider = models.OneToOneField(
        Usuario,
        on_delete=models.SET_NULL,
        null = True,
        blank= True,
        related_name='lideranca_equipe'
        )

    membros = models.ManyToManyField(Usuario, related_name='membros_equipe', blank=True)
    def __str__(self):
        return f"{self.nome} - {self.projeto.titulo}"





