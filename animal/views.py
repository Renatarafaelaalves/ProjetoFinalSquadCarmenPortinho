from django.shortcuts import render
from animal.models import Animal

def listar_animais(request):
    animais = Animal.objects.filter(adotado=False)
    contexto = {
        'animais': animais,
    }
    return render(request, 'lista_animais.html', contexto)

def ver_animal(request, id_animal):
    animal = Animal.objects.get(id=id_animal)
    return render(request, 'ver_animal.html', {'animal': animal})

def pagina_inicial(request):
    animais = Animal.objects.all()
    return render(request, 'seuapp/index.html', {'animais': animais})


