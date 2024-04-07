from django import forms
from .models import Adotante, SolicitacaoAdocao

class AdotanteForm(forms.ModelForm):
    class Meta:
        model = Adotante
        fields = ['nome', 'email', 'senha', 'endereco', 'outros_animais']
        widgets = {'senha': forms.PasswordInput()}


class SolicitacaoAdocaoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoAdocao
        fields = ['animal', 'adotante', 'status', 'aprovado_por']
        widgets = {'status': forms.TextInput(attrs={'disabled': 'disabled'})}