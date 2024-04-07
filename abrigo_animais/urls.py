from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('adocao/', include('adocao.urls', namespace='adocao')),  
    path('animais/', include('animal.urls', namespace='animais')),    
]



