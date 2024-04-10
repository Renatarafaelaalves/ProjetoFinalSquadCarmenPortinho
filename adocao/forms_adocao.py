from django import forms
from .models import SolicitacaoAdocao

class SolicitacaoAdocaoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoAdocao
        fields = ['nome', 'email', 'endereco', 'outros_animais', 'animal']
        widgets = {'status': forms.TextInput(attrs={'disabled': 'disabled'})}