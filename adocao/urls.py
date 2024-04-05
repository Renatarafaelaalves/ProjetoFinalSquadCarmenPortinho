from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_adocao, name='home_adocao'),  
    path('lista_animais/', views.lista_animais, name='lista_animais'),
    path('adotar_animal/<int:id_animal>/', views.adotar_animal, name='adotar_animal'),
]

