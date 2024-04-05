from django.urls import path
from animal.views import listar_animais, ver_animal

app_name = 'Animais'
urlpatterns = [
    path('animais/', listar_animais, name='listar_animais'),
    path('ver_animal/<int:id_animal>/', ver_animal, name='ver_animal')
]

