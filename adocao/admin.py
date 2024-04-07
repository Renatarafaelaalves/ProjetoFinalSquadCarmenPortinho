from django.contrib import admin
from adocao.models import CustomUser, SolicitacaoAdocao

@admin.register(CustomUser)
class AdotanteAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'endereco', 'outros_animais']
    search_fields = ['username', 'email']
    list_filter = ['username']

@admin.register(SolicitacaoAdocao)
class SolicitacaoAdocaoAdmin(admin.ModelAdmin):
    list_display = ['adotante_username', 'animal_nome', 'status', 'data_adocao','aprovador_por_username']
    search_fields = ['adotante__username', 'status']
    list_filter = ['data_adocao']
    list_editable = ['status']

    def salvar_status(self, request, obj):
        if obj.status in ['Aprovada', 'Recusada'] and not obj.aprovado_por:
            obj.aprovado_por = request.user
        obj.save()

    def adotante_username(self, obj):
        return obj.adotante.username
    
    def animal_nome(self, obj):
        return obj.animal.nome
    
    def aprovador_por_username(self, obj):
        return obj.aprovador_por.username if obj.aprovador_por else '-'