from django.urls import path
from animal.views import listar_animais, ver_animal, pagina_inicial

app_name = 'animais'
urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('listar_animais/', listar_animais, name='listar_animais'),
    path('<int:id_animal>/', ver_animal, name='ver_animal')
]