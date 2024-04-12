from django.db import models

class FormularioVoluntario(models.Model):
    opcoes_disponibilidade = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite')
    ]

    opcoes_experiencia = [
        ('sim', 'Sim'),
        ('não', 'Não'),
    ]

    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    endereco = models.CharField(max_length=100)
    motivo = models.TextField()
    disponibilidade = models.CharField(max_length=5, choices=opcoes_disponibilidade)
    experiencia =  models.CharField(max_length=3, choices=opcoes_experiencia)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Solicitação de voluntariado'
        verbose_name_plural = 'Solicitações de voluntariado'
        ordering = ['-data']