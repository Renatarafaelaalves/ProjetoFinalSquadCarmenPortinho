from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioVoluntarioForm
from .models import FormularioVoluntario

def formulario_voluntario(request):
    opcoes_disponibilidade = FormularioVoluntario.opcoes_disponibilidade
    opcoes_experiencia = FormularioVoluntario.opcoes_experiencia

    if request.method == 'POST':
        form = FormularioVoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitação de adoção enviada com sucesso!')
            return redirect('animais')
    else:
        form = FormularioVoluntarioForm()
    contexto = {
        'form': form,
        'opcoes_disponibilidade': opcoes_disponibilidade,
        'opcoes_experiencia': opcoes_experiencia
    }
    return render(request, 'cadastro.html', contexto)