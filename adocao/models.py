from django.db import models
from django.contrib.auth.models import User

class Adotante(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    outros_animais = models.IntegerField(default=0)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nome}[{self.email}]'
    class Meta:
        verbose_name = 'Cadastro de adotante'
        verbose_name_plural = 'Cadastro de adotantes'
        ordering = ['-data']

class SolicitacaoAdocao(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Aprovada', 'Aprovada'),
        ('Recusada', 'Recusada'),
    )

    data_adocao = models.DateField(auto_now_add=True)
    animal = models.ForeignKey('animal.Animal', on_delete=models.CASCADE)
    adotante = models.ForeignKey('Adotante', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    aprovado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Solicitação de Adoção de {self.animal.nome} por {self.adotante.nome} realizada com sucesso, aguardando aprovação."