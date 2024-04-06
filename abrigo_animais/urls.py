from django.contrib import admin
from django.urls import path, include
from animal.views import listar_animais
from adocao.views import home_adocao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_animais, name='listar_animais'),  
    path('adocao/', home_adocao, name='home_adocao'),  
    path('animais/', include('animal.urls')),  
    path('adocao/', include('adocao.urls')),  
]



