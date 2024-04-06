from django.db import models
from django.contrib.auth.models import User

class Adocao(models.Model):
    data_adocao = models.DateField()
    animal = models.ForeignKey('animal.Animal', on_delete=models.CASCADE)
    adotante = models.ForeignKey('PerfilAdotante', on_delete=models.CASCADE)
    adocao_bemsucedida = models.BooleanField(default=False)

class PerfilAdotante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

class StatusAdocao(models.Model):
    animal = models.ForeignKey('animal.Animal', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)

class FeedbackAdocao(models.Model):
    adocao = models.OneToOneField('Adocao', on_delete=models.CASCADE)
    comentario = models.TextField()

class FormularioAdocao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField()



