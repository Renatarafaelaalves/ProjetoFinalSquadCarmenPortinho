from django.shortcuts import render, redirect, get_object_or_404
from animal.models import Animal
from .forms import FormularioAdocao

def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, 'adocao/lista_animais.html', {'animais': animais})

def detalhes_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'adocao/detalhes_animal.html', {'animal': animal})

def confirmacao_adocao(request):
    return render(request, 'adocao/confirmacao_adocao.html')

def home_adocao(request):
    animais = Animal.objects.all()  
    return render(request, 'adocao/home_adocao.html', {'animais': animais})

def mostrar_adocao(request):
    animais = Animal.objects.all()
    return render(request, 'adocao/mostrar_adocao.html', {'animais': animais})

def adotar_animal(request):
    if request.method == 'POST':
        form = FormularioAdocao(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacao_adocao')
    else:
        form = FormularioAdocao()
    
    return render(request, 'adocao/adotar_animal.html', {'form': form})

