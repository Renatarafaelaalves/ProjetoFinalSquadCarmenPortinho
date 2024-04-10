from django.contrib import admin
from .models import FormularioVoluntario

@admin.register(FormularioVoluntario)
class FormularioVoluntarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'disponibilidade', 'experiencia']
    search_fields = ['nome', 'animal' 'disponibilidade']
    list_filter = ['data']