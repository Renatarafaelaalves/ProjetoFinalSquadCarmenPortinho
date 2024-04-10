from django.urls import path
from .views import formulario_voluntario

app_name = 'voluntarios'
urlpatterns = [
    path('', formulario_voluntario, name='formulario_voluntario'),
]