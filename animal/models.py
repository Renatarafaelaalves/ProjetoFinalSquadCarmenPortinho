from django.db import models

# Create your models here.
class HitoricoSaude(models.Model):
    choices_castracao = (('C', 'Castrado'),
                        ('N', 'Não castrado'))
    castrado = models.CharField(max_length=1, choices=choices_castracao, default='N')
    vacinas = models.CharField(max_length=200)
    idas_vet = models.TextField()

    class Meta:
        verbose_name = 'Histórico de saúde'
        verbose_name_plural = 'Histórico de saúde'
    
class Animal(models.Model):
    choices_sexo = (('F', 'Fêmea'),
                        ('M', 'Macho'))
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    idade = models.IntegerField()
    raca = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    historico_saude = models.ForeignKey(HitoricoSaude, on_delete=models.CASCADE)
    adotado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering = ['nome']