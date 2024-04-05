from django.contrib import admin
from .models import Adocao, PerfilAdotante, FormularioAdocao, StatusAdocao, FeedbackAdocao

@admin.register(Adocao)
class AdocaoAdmin(admin.ModelAdmin):
    list_display = ['data_adocao', 'animal', 'adotante', 'adocao_bemsucedida']
    list_filter = ['data_adocao', 'adocao_bemsucedida']

@admin.register(PerfilAdotante)
class PerfilAdotanteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'endereco', 'telefone']

@admin.register(FormularioAdocao)
class FormularioAdocaoAdmin(admin.ModelAdmin):
    list_display = ['adotante', 'motivo', 'experiencia_anterior', 'outros_animais']

@admin.register(StatusAdocao)
class StatusAdocaoAdmin(admin.ModelAdmin):
    list_display = ['animal', 'status']
    list_filter = ['status']

@admin.register(FeedbackAdocao)
class FeedbackAdocaoAdmin(admin.ModelAdmin):
    list_display = ['adocao', 'comentario']
