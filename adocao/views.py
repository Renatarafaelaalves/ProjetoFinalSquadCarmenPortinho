from django.shortcuts import render, redirect
from django.contrib import messages
from .forms_adocao import SolicitacaoAdocaoForm  # Importe do novo arquivo forms_adocao.py
from animal.models import Animal
import os
from django.http import JsonResponse
from django.conf import settings

def solicitar_adocao(request):
    animais_disponiveis = Animal.objects.filter(adotado=False)
    if request.method == 'POST':
        form = SolicitacaoAdocaoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'solicitar_adocao.html', {'alerta_sucesso': True})
    else:
        form = SolicitacaoAdocaoForm()

    contexto = {
        'form': form,
        'animais_disponiveis': animais_disponiveis,
    }
    return render(request, 'solicitar_adocao.html', contexto)

