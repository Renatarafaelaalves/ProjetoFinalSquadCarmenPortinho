from django import forms 

class FormularioAdocao(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=15)
    mensagem = forms.CharField(widget=forms.Textarea)
