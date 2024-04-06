from django.contrib import admin
from .models import FormularioAdocao

class FormularioAdocaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'mensagem')  

admin.site.register(FormularioAdocao, FormularioAdocaoAdmin)

