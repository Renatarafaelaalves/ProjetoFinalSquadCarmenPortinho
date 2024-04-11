from django import forms
from .models import FormularioVoluntario

class FormularioVoluntarioForm(forms.ModelForm):
    class Meta:
        model = FormularioVoluntario
        fields = ['nome', 'email', 'endereco', 'motivo', 'disponibilidade', 'experiencia']