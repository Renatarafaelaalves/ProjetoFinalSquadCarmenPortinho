from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class CustomUser(AbstractUser):
    endereco = models.CharField(max_length=100)
    outros_animais = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Cadastro de adotante'
        verbose_name_plural = 'Cadastro de adotantes'

class SolicitacaoAdocao(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Aprovada', 'Aprovada'),
        ('Recusada', 'Recusada'),
    )

    data_adocao = models.DateField(auto_now_add=True)
    animal = models.ForeignKey('animal.Animal', on_delete=models.CASCADE)
    adotante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='solicitacoes_de_adocao')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    aprovado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='aprovacoes_de_adocao')

    def __str__(self):
        return f"Solicitação de Adoção de {self.animal.nome} por {self.adotante.username} realizada com sucesso, aguardando aprovação."