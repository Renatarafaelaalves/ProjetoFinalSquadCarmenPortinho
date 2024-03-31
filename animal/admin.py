from django.contrib import admin
from animal.models import HitoricoSaude, Animal

# Register your models here.
@admin.register(HitoricoSaude)
class HistoricoSaudeAdmin(admin.ModelAdmin):
    list_display = ['castrado', 'vacinas', 'idas_vet']

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'especie', 'idade', 'raca', 'data_cadastro', 'historico_saude']
    search_fields = ['especie','idade', 'raca']
    list_filter = ['data_cadastro']