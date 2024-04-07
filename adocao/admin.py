from django.contrib import admin
from .models import Adotante, SolicitacaoAdocao

@admin.register(Adotante)
class AdotanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']

@admin.register(SolicitacaoAdocao)
class SolicitacaoAdocaoAdmin(admin.ModelAdmin):
    list_display = ['adotante_nome', 'animal_nome', 'status', 'data_adocao','aprovador_por_username']
    search_fields = ['adotante_nome', 'status']
    list_filter = ['data_adocao']
    list_editable = ['status']

    def salvar_status(self, request, obj):
        if obj.status in ['Aprovada', 'Recusada'] and not obj.aprovado_por:
            obj.aprovado_por = request.user
        obj.save()

    def adotante_nome(self, obj):
        return obj.adotante.nome
    
    def animal_nome(self, obj):
        return obj.animal.nome
    
    def aprovador_por_username(self, obj):
        return obj.aprovador_por.username if obj.aprovador_por else '-'