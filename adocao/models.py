from django.db import models
from django.contrib.auth.models import User

class SolicitacaoAdocao(models.Model):

    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Aprovada', 'Aprovada'),
        ('Recusada', 'Recusada'),
    )

    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    endereco = models.CharField(max_length=100)
    outros_animais = models.IntegerField(default=0)
    animal = models.ForeignKey('animal.Animal', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    aprovado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitação de Adoção de {self.animal.nome} por {self.nome} realizada com sucesso, aguardando aprovação."
    
    class Meta:
        verbose_name = 'Solicitação de adoção'
        verbose_name_plural = 'Solicitações de adoção'
        ordering = ['-data']