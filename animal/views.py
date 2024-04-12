from django.shortcuts import render
from animal.models import Animal

def pagina_inicial(request):    
    if 'especie' in request.GET:
        especie = request.GET.get('especie', '')
        animais = Animal.objects.filter(especie__icontains=especie)
        contexto = {
            'animais': animais,
        }
        return render(request, 'lista_animais.html', contexto)
    
    return render(request, 'home.html')

def listar_animais(request):
    especies = request.GET.get('especie') 
    animais = Animal.objects.filter(adotado=False)
    
    if especies:
        animais = animais.filter(especie=especies)

    contexto = {
        'animais': animais,
    }
    return render(request, 'lista_animais.html', contexto)

def ver_animal(request, id_animal):
    animal = Animal.objects.get(id=id_animal)
    return render(request, 'ver_animal.html', {'animal': animal})



