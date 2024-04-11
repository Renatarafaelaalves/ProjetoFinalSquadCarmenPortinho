from django.urls import path
from .views import solicitar_adocao

app_name = 'adocao'
urlpatterns = [
    path('', solicitar_adocao, name='solicitar_adocao'),
    
]
