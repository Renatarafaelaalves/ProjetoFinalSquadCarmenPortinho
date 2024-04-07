from django.urls import path
from . import views

app_name = 'adocao'
urlpatterns = [
    path('', views.home_adocao, name='home_adocao'),  
    path('cadastro/', views.cadastro_adotante, name='cadastro_adotante'),
    path('adotar/', views.solicitar_adocao, name='solicitar_adocao'),
    path('status/', views.consultar_status, name='consultar_status'),
    path('confirmacao/', views.confirmacao_adocao, name='confirmacao_adocao'),
    path('login/', views.login_adotante.as_view(), name='login'),
]

