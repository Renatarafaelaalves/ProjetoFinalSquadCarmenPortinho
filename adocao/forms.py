from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SolicitacaoAdocao, CustomUser

class AdotanteForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'endereco', 'outros_animais']


class SolicitacaoAdocaoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoAdocao
        fields = ['animal', 'adotante', 'status', 'aprovado_por']
        widgets = {'status': forms.TextInput(attrs={'disabled': 'disabled'})}