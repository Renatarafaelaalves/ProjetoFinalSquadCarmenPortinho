from django.urls import path
from animal.views import mostrar_animais

app_name = 'Animais'
urlpatterns = [
    path('mostrar_animais/', mostrar_animais, name='mostrar_animais')
]