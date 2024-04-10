from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('animal.urls',)),
    path('admin/', admin.site.urls), 
    path('adocao/', include('adocao.urls', namespace='adocao')),  
    path('animais/', include('animal.urls', namespace='animais')),
    path('voluntarios/', include('voluntarios.urls', namespace='voluntarios')),      
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)