from django.shortcuts import render
from animal.models import Animal
# Create your views here.

def mostrar_animais(request):
    animais = Animal.objects.all()
    contexto = {
        'animais': animais,
    }
    return render(request, 'mostrar_animais.html', contexto)

def ver_animal(request, id_animal):
    animal = Animal.objects.get(id=id_animal)
    return render(request, 'ver_animal.html', {'animal':animal})