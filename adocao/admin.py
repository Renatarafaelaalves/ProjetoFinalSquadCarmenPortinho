from django.contrib import admin
from .models import SolicitacaoAdocao

@admin.register(SolicitacaoAdocao)
class SolicitacaoAdocaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'animal_nome', 'status', 'data']
    search_fields = ['nome', 'animal' 'status']
    list_filter = ['data']
    list_editable = ['status']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.status == 'Aprovada':
            obj.animal.adotado = True
            obj.animal.save()
        elif obj.status == 'Recusada':
            obj.animal.adotado = False
            obj.animal.save()
            obj.aprovado_por = None
            obj.save()

    def animal_nome(self, obj):
        return obj.animal.nome