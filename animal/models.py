from django.db import models

# Create your models here.
class HitoricoSaude(models.Model):
    choices_castracao = (('C', 'Castrado'),
                        ('N', 'Não castrado'))
    castrado = models.CharField(max_length=1, choices=choices_castracao, default='N')
    vacinas = models.CharField(max_length=200)
    idas_vet = models.TextField()

    def __str__(self):
        return f'{self.castrado}'
    

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    idade = models.IntegerField()
    raca = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    historico_saude = models.ForeignKey(HitoricoSaude, on_delete=models.CASCADE)
