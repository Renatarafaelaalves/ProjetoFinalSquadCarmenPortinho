from django.urls import path
from animal.views import mostrar_animais, ver_animal

app_name = 'Animais'
urlpatterns = [
    path('animais/', mostrar_animais, name='mostrar_animais'),
    path('ver_animal/<int:id_animal>/', ver_animal, name='ver_animal')
]
