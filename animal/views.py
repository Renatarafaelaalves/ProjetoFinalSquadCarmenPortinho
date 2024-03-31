from django.shortcuts import render
from animal.models import Animal
# Create your views here.

def mostrar_animais(request):
    animais = Animal.objects.all()
    contexto = {
        'animais': animais,
    }
    return render(request, 'mostrar_animais.html', contexto)
