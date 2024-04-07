from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('animais/', include('animal.urls')),  
    path('adocao/', include('adocao.urls')),  
]



